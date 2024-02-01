import os
import mysql.connector
from dotenv import load_dotenv
from mysql.connector import Error

load_dotenv()


MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_DB = os.getenv("MYSQL_DB")
MYSQL_PASS= os.getenv("MYSQL_PASS")


def connectToDb():
    try:
        db = mysql.connector.connect(
            host = MYSQL_HOST,
            user = MYSQL_USER,
            database = MYSQL_DB,
            password = MYSQL_PASS
        )
        
        if db.is_connected():
            print('Connection Succesfully')
            return db
    
    except Error as e:
        print(f'Error while connection to DB: {e}')    
    
    