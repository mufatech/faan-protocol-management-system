import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

# Establish connection
connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

# Create cursor
cursor = connection.cursor()

# Execute SQL query
cursor.execute("SHOW TABLES")

# Fetch and display results
tables = cursor.fetchall()

for table in tables:
    print(table[0])

# Close the cursor and connection
cursor.close()
connection.close()