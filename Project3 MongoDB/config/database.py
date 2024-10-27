# Step : 2
from pymongo.mongo_client import MongoClient

client = MongoClient("mongodb+srv://nizum:5kXPMsQBqhf65LZr@cluster0.4fphg1c.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.employees

collection_name = db["employee"]