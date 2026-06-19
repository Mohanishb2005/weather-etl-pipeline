import psycopg2

try:
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="12345",
        host="localhost",
        port="5432"
    )

    print("Connection Successful!")

    conn.close()

except Exception as e:
    print(e)