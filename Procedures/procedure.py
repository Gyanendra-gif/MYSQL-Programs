"""
@Author: Gyanendra
@Date: 02/01/2022
@Last Modified by: Gyanendra
@Last Modified time: 02/01/2022 
@Title : Procedures Programs in Python
"""

import mysql.connector as con

connection = con.connect(host='localhost',database='mobile_data',user='root',password='Janu@1252')
cursor= connection.cursor()

def insert():
    """
    Description:
        Function is used to insert data into the table after taking input from the user
    Parameter:
        None
    Return:
        None
    """
    name = input("Enter the Name of Mobile: ")
    price = int(input("Enter the Price of Mobile: "))
    model = input("Enter the Model of Mobile: ")

    try:
        args = (name,price,model)    
        cursor.callproc("insert_data", args) # TO Call Procedure
        connection.commit()         # This method sends a COMMIT statement to the MySQL server, committing the current transaction
        print("Data Inserted Successfully")
    except Exception as e:
        print(e)

def read():
    """
    Description:
        Function is used to read data of the table
    Parameter:
        None
    Return:
        None
    """
    try:
        cursor.callproc("read_data")
        for item in cursor.stored_results():
            print(item.fetchall())
    except Exception as e:
        print(e)

def delete():
    """
    Description:
        Function is used to delete data from the table after taking id from the user
    Parameter:
        None
    Return:
        None
    """
    key=int(input("Enter id of Mobile to delete data: "))
    try:
        args=(key,)
        cursor.callproc("delete_data", args)
        connection.commit()
        print("Data Removed Successfully")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    condition = True
    while (condition == True):
        try:
            choice = int(input("Enter your choice to perform operation, \n 1)Insert \n 2)Read \n 3)Delete:-"))
            if (choice==1):
                insert()
            elif (choice==2):
                read()
            elif (choice==3):
                delete()
            else:
                print('Enter Correct Option')
            userChoice = int(input('Press 0 to Continue the Program or 1 to stop the program: '))
            if (userChoice == 1):
                condition = False 
        except ValueError:
            print("Error!, Entered Value is not Integer")   