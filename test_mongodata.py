
import sys
from pymongo.mongo_client import MongoClient
import os
from dotenv import load_dotenv


from networksecurity.exception.exception import NetworkSecurityException
import certifi
# Load environment variables from .env file
load_dotenv()
uri = os.getenv("MONGODB_URI")

# Create a new client and connect to the server
client = MongoClient(uri, tlsCAFile=certifi.where() )

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    raise NetworkSecurityException(e, sys) from e
    