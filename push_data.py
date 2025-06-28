import os 
import sys
from dotenv import load_dotenv
import json
load_dotenv()  # Load environment variables from .env file
MONGODB_URI = os.getenv("MONGODB_URI")

from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException


import certifi
ca = certifi.where()

import pymongo
import pandas as pd
import numpy as np


class NetworkSecurityData:
    def __init__(self):
        try:
           pass
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e

    def cv_to_convert_to_json(self, file_path):
        try:
            df = pd.read_csv(file_path)
            df.reset_index(drop=True, inplace=True)
            records = list(json.loads(df.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys) from e
        
    def push_data_to_mongodb(self, data, db_name: str, collection_name: str):
        try:

            self.data = data
            self.db_name = db_name  
            self.collection_name = collection_name
            self.client = pymongo.MongoClient(MONGODB_URI , tlsCAFile=ca)
            self.db = self.client[self.db_name]
            self.collection = self.db[self.collection_name]
            self.collection.insert_many(self.data)
            logging.info(f"Data pushed to MongoDB collection '{self.collection_name}' in database '{self.db_name}' successfully.")
            return True
        except Exception as e:
            logging.error(f"Error pushing data to MongoDB: {e}")
            raise NetworkSecurityException(e, sys) from e
        
if __name__ == "__main__":
    try:
        file_path = "Network_data\phisingData.csv"
        db_name = "network_security_db"
        collection_name = "network_security_collection"

        network_security_data = NetworkSecurityData()
        data = network_security_data.cv_to_convert_to_json(file_path)
       
        bin = network_security_data.push_data_to_mongodb(data, db_name, collection_name)
        print(f"Data pushed successfully, total records: {bin}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")