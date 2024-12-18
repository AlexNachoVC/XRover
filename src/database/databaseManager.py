import os
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve database connection details from environment variables
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')

class DatabaseManager:
    def __init__(self, host, database, user, password):
        # Initialize the DatabaseManager with connection details
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None
        self.connect()

    def connect(self):
        # Establish a connection to the database
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            if self.connection.is_connected():
                print("Connected to the database")
                self.cursor = self.connection.cursor()
        except Error as e:
            print(f"Error: {e}")

    def get_connection(self):
        # Return the current database connection
        return self.connection
    
    def disconnect(self):
        # Close the database connection
        if self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            print("Disconnected from the database")
