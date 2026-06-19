CREATE DATABASE weather_db;

CREATE TABLE weather_data(
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP,
    temperature FLOAT,
    weather_category VARCHAR(50)
);