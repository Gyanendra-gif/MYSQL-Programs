"""
@Author: Gyanendra
@Date: 02/01/2022
@Last Modified by: Gyanendra
@Last Modified time: 02/01/2022 
@Title : Function Programs in Python
"""

import mysql.connector as con

connection = con.connect(host='localhost',database='hotel',user='root',password='Janu@1252')
cursor= connection.cursor()

def function():
    """
    Description:
        Function is used to fetch data of the table after using function
    Parameter:
        None
    Return:
        None
    """
    sql = "select cname, age, customer_occupation(age) from customer;"
    try:
        cursor.execute(sql)
        data=cursor.fetchall()
        for item in data:
            print(item)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    function()