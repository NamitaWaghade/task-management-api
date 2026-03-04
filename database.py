# from pymongo import MongoClient
# import certifi

# MONGO_URL = "mongodb+srv://namita_user:Nrwaghade616@cluster0.a5ccl6z.mongodb.net/taskdb?retryWrites=true&w=majority&appName=Cluster0"

# client = MongoClient(
#     MONGO_URL,
#     tls=True,
#     tlsCAFile=certifi.where()
# )

# db = client["taskdb"]
# collection = db["tasks"]
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import certifi

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

client = MongoClient(
    MONGO_URL,
    tls=True,
    tlsCAFile=certifi.where()
)

db = client["taskdb"]
collection = db["tasks"]

