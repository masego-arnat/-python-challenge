import pandas as pd
from pymongo import MongoClient
import pymongo
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from fastapi import FastAPI, HTTPException
from bson import ObjectId
 
 # Initialize FastAPI  
app = FastAPI()
#  connection string 
uri = "mongodb+srv://masegoarnat:Masego1234@cluster1.f3nzl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


 
# Endpoint to fetch data and return as a Pandas DataFrame
@app.get("/fetch-all-data")
def fetch_all_data():
    try:
         # Access a database 
        db = client.python

        # Access a collection 
        collection = db.Wine
        # Fetch all documents from the collection
        documents = list(collection.find())

        
     # Convert ObjectId to string (for JSON serialization)
        for doc in documents:
            doc["_id"] = str(doc["_id"])

        # Convert to a Pandas DataFrame 
        df = pd.DataFrame(documents)

        # Convert DataFrame to JSON
        result = df.to_dict(orient="records")

        # Return the data as a JSON response
       
        return {"status": "success", "data": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# Endpoint to fetch a single item by ID
@app.get("/fetch-item/{item_id}")
def fetch_item(item_id: str):
    try:
        # Access the database and collection
        db = client.python
        collection = db.Wine

        # Fetch a single document by _id
        document = collection.find_one({"_id": ObjectId(item_id)})

        # Check if the document exists
        if document:
            # Convert ObjectId to string (for JSON serialization)
            document["_id"] = str(document["_id"])
            return {"status": "success", "data": document}
        else:
            raise HTTPException(status_code=404, detail="Item not found")
    except Exception as e:
        return {"status": "error", "message": str(e)}
# Run the FastAPI app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)











 