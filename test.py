import pandas as pd
from pymongo import MongoClient
import pymongo
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

#  connection string 
uri = "mongodb+srv://masegoarnat:Masego1234@cluster1.f3nzl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print(" You successfully connected to MongoDB!")
    # Access a database 
    db = client.python

    # Access a collection 
    collection = db.Wine
    
    # Fetch all documents in the collection
    documents = collection.find()
    # Convert MongoDB documents to a Pandas DataFrame
    df = pd.DataFrame(list(documents))
    # Print the DataFrame
    print(df)
    # Close the connection
    client.close()

    # # Iterate through the documents and print them
    # for doc in documents:
    #  print("----------",doc)
except Exception as e:
    print(e)









 












 