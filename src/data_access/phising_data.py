import sys
from typing import Optional, List

from database_connect import mongo_operation as mongo
from pymongo import MongoClient
import numpy as np
import pandas as pd
from src.constant import *
from src.configuration.mongo_db_connection import MongoDBClient
from src.exception import CustomException
import os


class PhisingData:
    """
    This class help to export entire mongo db record as pandas dataframe
    """

    def __init__(self,
                 database_name: str):
        # setting address of database
        try:

            self.database_name = database_name
            self.mongo_url = os.getenv("MONGO_DB_URL")

        except Exception as e:
            raise CustomException(e, sys)

    def get_collection_names(self) -> List:
    # conects to db and return list of items of connected db
        mongo_db_client = MongoClient(self.mongo_url)
        collection_names = mongo_db_client[self.database_name].list_collection_names()
        return collection_names

    def get_collection_data(self,
                            collection_name: str) -> pd.DataFrame:

        mongo_connection = mongo(
            client_url=self.mongo_url,
            database_name=self.database_name,
            collection_name=collection_name
        )
        df = mongo_connection.find() # every single row of data to dataframe

        if "_id" in df.columns.to_list():
            df = df.drop(columns=["_id"])
        df = df.replace({"na": np.nan}) # replaces "na" with nan(not a number)
        return df


# Generator use to return data
    def export_collections_as_dataframe(
            self) -> pd.DataFrame:
        try:
            """
            export entire collectin as dataframe:
            return dd.DataFrame of collection
            """

            collections = self.get_collection_names()

            for collection_name in collections:
                df = self.get_collection_data(collection_name=collection_name)
                yield collection_name, df

        except Exception as e:
            raise CustomException(e, sys)


'''The Exact Execution Flow

Initialize: Grabs the Database Name and your secret Connection URL from the system.

Scan: Connects to Atlas and gets a List of every collection name (table) in that database.

Loop: Iterates through every name in that list one by one.

Fetch & Clean: For each name:

Downloads all records into a Pandas DataFrame.

Deletes the _id column.

Replaces any "na" text with actual NaN values.

Yield: Returns the (Collection Name, DataFrame) pair and "pauses" the code until the next part of your pipeline is ready for the next table.'''