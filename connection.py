"""
@Author: Gyanendra
@Date: 10/01/2021 
@Last Modified by: Gyanendra
@Last Modified time: 27/01/2022 
@Title : SQL Programs in Python
"""
import mysql.connector
from mysql.connector import Error

def connection():
    
    try:
        connection = mysql.connector.connect(host='localhost',
                                            database='payroll_services',
                                            user='root',
                                            password='Janu@1252')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    connection()            