# load.py

import pandas as pd
import psycopg2

conn = psycopg2.connect(
    database="weather_db",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
)

df = pd.read_csv("weather_clean.csv")

cursor = conn.cursor()

for index, row in df.iterrows():

    cursor.execute(
        """
        INSERT INTO weather_data
        (timestamp, temperature, weather_category)

        VALUES (%s,%s,%s)
        """,

        (
            row["time"],
            row["temperature"],
            row["weather_category"]
        )
    )

conn.commit()

cursor.close()
conn.close()