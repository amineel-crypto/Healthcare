from fastapi import FastAPI
import mysql.connector
import uvicorn

app = FastAPI()

@app.get("/fetch_data")
def fetch_data():
    try:
        # Connect to the MySQL database
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="2004",
            database="medical_db"
        )
        cursor = conn.cursor(dictionary=True)  # Fetch rows as dictionaries

        # Query the database
        cursor.execute("SELECT * FROM doctors")  # Replace 'doctors' with your table name
        rows = cursor.fetchall()

        # Return the data as JSON
        return {"status": "success", "data": rows}

    except mysql.connector.Error as e:
        # Return an error response
        return {"status": "error", "message": str(e)}

    finally:
        # Ensure resources are cleaned up
        if 'cursor' in locals():
            cursor.close()
        if 'conn' in locals() and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    uvicorn.run("PI:app", host="127.0.0.1", port=8000, reload=True)