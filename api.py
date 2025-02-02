import requests
import pandas as pd

# # Fetch data from the FastAPI endpoint
# response = requests.get("http://127.0.0.1:8000/fetch-all-data")

# if response.status_code == 200:
#     data = response.json()["data"]  # Extract the "data" field
#     df = pd.DataFrame(data)  # Convert to DataFrame
#     print(df)
# else:
#     print(f"Error: {response.status_code}")

url = 'http://127.0.0.1:8000/create-item'
data = {
    "wine": 33333,
    "alcohol": 14.23,
    "malic_acid": 1.71,
    "ash": 2.43,
    "alcalinity_ash": 15.6,
    "mg": 127,
    "phenols": 2.8,
    "flavanoids": 3.06,
    "nonflavanoid_phenols": 0.28,
    "proanth": 2.29,
    "color_intensity": 5.64,
    "hue": 1.04,
    "od": 3.92,
    "proline": 1065
}
 
 
response = requests.post(url, json=data)


 # Print response to the screen
if response.status_code == 200:
    result = response.json()
    print("✅ Success!")
    print(f"Message: {result['message']}")
    print(f"Inserted ID: {result['inserted_id']}")
else:
    print("❌ Error:", response.status_code, response.text)
 