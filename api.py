import requests
import pandas as pd

# Fetch data from the FastAPI endpoint
response = requests.get("http://127.0.0.1:8000/fetch-all-data")

if response.status_code == 200:
    data = response.json()["data"]  # Extract the "data" field
    df = pd.DataFrame(data)  # Convert to DataFrame
    print(df)
else:
    print(f"Error: {response.status_code}")