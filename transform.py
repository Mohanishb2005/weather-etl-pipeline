# transform.py

import pandas as pd

df = pd.read_csv("weather.csv")
df["time"] = pd.to_datetime(df["time"])

def weather_label(temp):

    if temp > 35:
        return "Hot"

    elif temp > 25:
        return "Moderate"

    else:
        return "Cold"
    
df["weather_category"] = df["temperature"].apply(weather_label)
print(df.head())  
df.to_csv("weather_clean.csv", index=False)