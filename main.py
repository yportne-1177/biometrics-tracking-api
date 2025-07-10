import os
from fastapi import FastAPI, HTTPException
import mysql.connector

app = FastAPI()

# Database configuration using environment variables
DB_CONFIG = {
    "host": os.environ.get("DB_HOST"),
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASSWORD"),
    "database": os.environ.get("DB_NAME")
}

# Function to get a new database connection
def get_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.get("/")
def read_root():
    return {"message": "Welcome to the BiometricsTracking API"}

@app.get("/tables", summary="List all tables in the database")
def list_tables():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES;")
        tables = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return {"tables": tables}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/data/{table_name}", summary="Get first 100 rows from a table")
def get_table_data(table_name: str):
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(f"SELECT * FROM `{table_name}` LIMIT 100;")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return rows
    except mysql.connector.Error as err:
        raise HTTPException(status_code=400, detail=f"MySQL error: {err}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
