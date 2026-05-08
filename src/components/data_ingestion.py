import sys
import os
import numpy as np 
import pandas as pd
from pymongo import MongoClient
from zipfile import Path
from src.constant import *
from src.exception import CustomException
from src.logger import logging

from src.data_access.phising_data import PhisingData
from src.utils.main_utils import MainUtils # save object
from dataclasses import dataclass # clean way to store.csv files(train,test)


@dataclass
class DataIngestionConfig:
    data_ingestion_dir: str = os.path.join(artifact_folder, "data_ingestion")
# defines where data should be stored in system


# using dataingestonconfig class by making it object inside dataingestion class
class DataIngestion:
    
    # setup phase
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig() # creating and stroing object
        self.utils = MainUtils()


    # download and save phase
    def export_data_into_raw_data_dir(self) -> pd.DataFrame:

        try:
            logging.info("Exporting data from MongoDB")

            raw_batch_files_path = (
            self.data_ingestion_config.data_ingestion_dir
            )
            os.makedirs(raw_batch_files_path, exist_ok=True)

            # accesing phisingdata.ipynb
            income_data = PhisingData(
            database_name=MONGO_DATABASE_NAME
            )

            logging.info(
                f"Saving exported data into feature store "
             f"file path: {raw_batch_files_path}"
            )

            for collection_name, dataset in (
                income_data.export_collections_as_dataframe()
            ):

                logging.info(
                    f"Shape of {collection_name}: {dataset.shape}"
                )

                feature_store_file_path = os.path.join(
                    raw_batch_files_path,
                    collection_name + ".csv"
                )

                print(
                    f"feature_store_file_path-----"
                    f"{feature_store_file_path}"
                )

                # Save dataframe as CSV
                dataset.to_csv(
                    feature_store_file_path,
                    index=False
                ) # converting df to csv for future use

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_ingestion(self) -> Path:
        """
            Method Name :   initiate_data_ingestion
            Description :   This method initiates the data ingestion components of training pipeline 
            Output      :   train set and test set are returned as the artifacts of data ingestion components
            On Failure  :   Write an exception log and then raise an exception
            
        """
        logging.info("Entered initiate_data_ingestion method of Data_Ingestion class")

        try:
            self.export_data_into_raw_data_dir()

            logging.info("Got the data from mongodb")

            logging.info(
                "Exited initiate_data_ingestion method of Data_Ingestion class"
            )

            return self.data_ingestion_config.data_ingestion_dir

        except Exception as e:
            raise CustomException(e, sys) from e

if __name__ == "__main__":
    ingestion = DataIngestion()
    ingestion.initiate_data_ingestion()
    
'''
Automates Data Retrieval: It securely connects to MongoDB Atlas to fetch every data collection available in your database.

Cleans and Saves: it removes database-specific noise (like _id), replaces missing values, and saves the results as local CSV files.

Orchestrates the Pipeline: It physically creates an artifact folder structure and returns its path to trigger the next stage of your machine learning project.

'''
