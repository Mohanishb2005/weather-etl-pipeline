import requests
import os
import pandas as pd

url = "https://api.open-meteo.com/v1/forecast?latitude=18.52&longitude=73.85&hourly=temperature_2m"

response = requests.get(url)

data = response.json()

df = pd.DataFrame({
    "time": data["hourly"]["time"],
    "temperature": data["hourly"]["temperature_2m"]
})

print(df.head())

df.to_csv("weather.csv", index=False)

print("Current Folder:", os.getcwd())
print("CSV Created Successfully")