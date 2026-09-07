# import os
# import mysql.connector
# from dotenv import load_dotenv

# load_dotenv()

# mydb = mysql.connector.connect(
#     host=os.getenv("DB_HOST"),
#     user=os.getenv("DB_USER"),
#     password=os.getenv("DB_PASSWORD"),
# )

# my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE IF NOT EXISTS faan_protocol")

# my_cursor.execute("SHOW DATABASES")

# for db in my_cursor:
#     print(db)