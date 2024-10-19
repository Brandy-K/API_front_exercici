import mysql.connector

def db_client():
    try:
        # Define the connection parameters correctly
        host = "localhost"
        port = "3306"
        user = "root"
        password = "password"
        database = "alumnat"
        collation = "utf8mb4_general_ci"

        # Establish and return the database connection
        return mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            charset=collation  # Use 'charset' instead of 'collation'
        )
    except mysql.connector.Error as e:
        return {"status": -1, "message": f"Connection error: {e}"}
