import pymongo
import pandas as pd

DB_NAME = "US_VISA"
COLLECTION_NAME = "visa_data"
CONNECTION_URL = "mongodb+srv://sujithlearnearn:lkevaBQjv2sGmdy8@clusterus-visa.ca8l7.mongodb.net/?retryWrites=true&w=majority&appName=Clusterus-visa"

# from pymongo.mongo_client import MongoClient
# uri = "mongodb+srv://sujithlearnearn:lkevaBQjv2sGmdy8@clusterus-visa.ca8l7.mongodb.net/?retryWrites=true&w=majority&appName=Clusterus-visa"
# # Create a new client and connect to the server
# client = MongoClient(uri)

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

df = pd.read_csv("notebook/Visadataset.csv")
data = df.to_dict(orient="records")

client = pymongo.MongoClient(CONNECTION_URL)
data_base = client[DB_NAME]
collection = data_base[COLLECTION_NAME]

rec = collection.insert_many(data)
print(rec)