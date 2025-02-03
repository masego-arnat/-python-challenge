import requests
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

from joblib import dump

# TODO: you should fetch the data from the MongoDB database
#  this is the end point to get the data locally 
 # # response = requests.get("http://127.0.0.1:8000/fetch-all-data")

# is the end poist that accessing the api when runing in the container
response = requests.get("http://container1.example:8000/fetch-all-data")

print("Response Status Code:", response.status_code)

try:
    response_json = response.json()  # Parse JSON response
    print("Full Response JSON:", response_json)  # Debugging step

    if "data" in response_json:
        data = response_json["data"]  # Extract the "data" field
        df = pd.DataFrame(data)  # Convert to DataFrame
        print(df)
    else:
        print("Error: 'data' key is missing in response JSON.")
except Exception as e:
    print(f"Error while parsing response JSON: {e}")
    print("Raw response text:", response.text)  # Show raw text in case it's not JSON

 

 

# set the features and labels
y = df["wine"]
X = df.drop(["_id"], axis=1)
 

# split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# train the model
model = KNeighborsClassifier(n_neighbors=20)
model.fit(X_train, y_train)

# see how the model performs on the training and test data
y_pred_test = model.predict(X_test)
y_pred_train = model.predict(X_train)
print(f"Training accuracy: {accuracy_score(y_train, y_pred_train)}")
print(f"Test accuracy: {accuracy_score(y_test, y_pred_test)}")

# save the model to file
# this model should be used when making predictions through the API
dump(model, "model.joblib")

# can be loaded with the following code:
# from joblib import load
# model = load("model.joblib")