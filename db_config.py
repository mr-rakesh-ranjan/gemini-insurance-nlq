from dotenv import load_dotenv, find_dotenv # type: ignore
import os
# Load environment variables from .env file.
load_dotenv(find_dotenv())

db_host = os.getenv('DB_SERVER')
db_name = os.getenv('DB_NAME')
db_username = os.getenv('DB_USERNAME')
db_pwd = os.getenv('DB_PWD')
db_driver = '{ODBC Driver 18 for SQL Server}'  # Update the driver as necessary



class Config:
    """
    Base configuration class.
    """
    TESTING = True
    DEBUG = True
    
    """
    Database configuration.
    """
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False