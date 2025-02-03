from urllib import request
from openai import BaseModel
import pandas as pd
from pymongo import MongoClient
import pymongo
from pymongo import MongoClient
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from fastapi import FastAPI, HTTPException, Request
from bson import ObjectId
 
 # Initialize FastAPI  
app = FastAPI()
#  connection string 
uri = "mongodb+srv://masegoarnat:Masego1234@cluster1.f3nzl.mongodb.net/?retryWrites=true&w=majority&tls=true"

# uri = "mongodb+srv://masegoarnat:Masego1234@cluster1.f3nzl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Connect to MongoDB
try:
    db = client.python
    test = db.Wine
except Exception as e:
 print("exeption ------------",e)

 # model for wine record
class Wine(BaseModel):
    wine: int
    alcohol: float
    malic_acid: float
    ash: float
    alcalinity_ash: float
    mg: int
    phenols: float
    flavanoids: float
    nonflavanoid_phenols: float
    proanth: float
    color_intensity: float
    hue: float
    od: float
    proline: int
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


@app.put("/update-item/{item_id}")
async def update_item(item_id: str, wine: Wine):
    try:
        # Convert item_id to ObjectId. Handle potential errors.
        try:
            object_id = ObjectId(item_id)
        except Exception as e:
            raise HTTPException(status_code=400, detail="Invalid item ID")

        result = test.update_one(
            {"_id": object_id},
            {"$set": wine.model_dump()}
        )

        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="No record found with the given ID")

        return {
            "message": "Wine record updated successfully",
            "updated_id": item_id
        }


    except Exception as e:
        return {"error": str(e)}  # For  unexpected exceptions
 

@app.delete("/delete-item/{item_id}")
async def delete_item(item_id: str):
    try:
        # Convert item_id to ObjectId and delete from MongoDB
        result = test.delete_one({"_id": ObjectId(item_id)})

        if result.deleted_count == 0:
            return {"error": "No record found with the given ID"}

        return {
            "message": "Wine record deleted successfully",
            "deleted_id": item_id
        }
    except Exception as e:
        return {"error": str(e)}


@app.post("/create-item")
async def create_item(request: Request):
    try:
        data = await request.json()  
        print("Received data:", data)

        # Insert data into MongoDB
        result = test.insert_one(data)

        return {
            "message": "Wine record created successfully",
            "inserted_id": str(result.inserted_id)  # Convert ObjectId to string
        }

    except Exception as e:
        return {"error": str(e)}









        
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











 