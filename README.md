# phishing-classifier
this is machine learning project 1



'''pip install -e .  ''' to run setup.py


Project Libraries
This section outlines the core technical stack used to build, serve, and monitor the Phishing Classifier.

Data Processing & Machine Learning
These libraries form the "brain" of the project, handling everything from raw data cleaning to complex pattern recognition.

Pandas: The primary tool for data manipulation and structured data analysis.

NumPy: Provides support for large multi-dimensional arrays and high-level mathematical functions.

Scikit-learn: A robust library for classical ML algorithms, preprocessing, and model evaluation.

XGBoost / CatBoost: Advanced gradient boosting frameworks used for high-accuracy classification on tabular data.

Web Development & API Handling
These tools transform the machine learning model into an accessible service.

Flask / FastAPI: Web frameworks used to build the application interface and manage API endpoints.

Requests: A simple library for sending HTTP requests to test or interact with external web services.

Uvicorn / Gunicorn: Production-grade servers used to host and scale the web application.

Database & Cloud Storage
Responsible for the persistent storage of logs, user data, and model artifacts.

SQLAlchemy: An ORM that simplifies SQL database interactions using Pythonic code.

PyMongo: The official driver for connecting to MongoDB, used for flexible, NoSQL data storage.

Boto3: The Amazon Web Services (AWS) SDK for interacting with S3 buckets and other cloud infrastructure.

Environment & Deployment Tools
Ensures the project is portable, configurable, and easy to deploy across different systems.

Python-dotenv: Securely loads environment variables (like API keys) from a .env file.

PyYAML: Handles configuration management by reading and writing YAML files.

Setuptools / Wheel: Standard tools for packaging the project into a distributable format.

Serialization & Asynchronous Processing
Handles the efficient saving of models and the management of concurrent tasks.

Joblib / Pickle: Used to save and load trained models, ensuring they don't need to be retrained every time the app starts.

Pydantic: Enforces strict data validation using Python type hints to prevent malformed API inputs.

Anyio / HTTPX: Libraries that enable asynchronous networking, allowing the app to handle multiple tasks at once.

Model Monitoring & Performance Tracking
Used to ensure the model remains accurate and reliable after it has been deployed.

Evidently: A powerful framework for evaluating model health, detecting "data drift," and generating visual reports on performance over time.