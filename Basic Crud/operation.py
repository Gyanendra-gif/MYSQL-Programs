"""
@Author: Gyanendra
@Date: 28/01/2022
@Last Modified by: Gyanendra
@Last Modified time: 01/01/2022 
@Title : SQL Programs in Python
"""
from random import choice
import mysql.connector as con

connection = con.connect(host='localhost',database='student_attendance',user='root',password='Janu@1252')
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
    name = input("Enter the Name of Student: ")
    rollNo = int(input("Enter Roll No. of Student: "))
    section = input("Enter Section of the Student: ")
    sql = "insert into student_data(name,rollno,section) values(%s,%s,%s)"
    value = (name,rollNo,section)
    try:
        cursor.execute(sql, value)  # TO Execute Query
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
    sql = "select * from student_data"
    try:
        cursor.execute(sql)
        data=cursor.fetchall()
        for item in data:
            print(item)
    except Exception as e:
        print(e)

def update():
    """
    Description:
        Function is used to update data of the table after taking id of student from the user
    Parameter:
        None
    Return:
        None
    """
    key=int(input("Enter id of student to update data: "))
    sql = "select * from student_data where id=%s"
    value = (key,)
    try:
        cursor.execute(sql,value)
        data=cursor.fetchall() # fetches all rows from the last executed statement.
        for item in data:
            name = item[1]
            rollNo = item[2]
            section = item[3]
            user_input = int(input("Enter your choice to update data \n 1)name \n 2)rollNo \n 3)section: "))
            if(user_input==1):
                name = input("Enter New Name: ")
            elif(user_input==2):
                rollNo = int(input("Enter New Roll No: ")) 
            elif(user_input==3):
                section = input("Enter New Section: ")
            else:
                print("Enter Correct Value")  
            sql = "update student_data set name=%s,rollNo=%s,section=%s where id=%s"
            value = (name,rollNo,section,key)
            try:
                cursor.execute(sql,value)
                connection.commit()
                print("Data Updated Successfully")
            except Exception as e:
                print(e)
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
    key=int(input("Enter id of student to delete data: "))
    sql = "delete from student_data where id=%s"
    value = (key,)
    try:
        cursor.execute(sql, value)
        connection.commit()
        print("Data Removed Successfully")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    condition = True
    while (condition == True):
        try:
            choice = int(input("Enter your choice to perform operation, \n 1)Insert \n 2)Read \n 3)Update \n 4)Delete:-"))
            if (choice==1):
                insert()
            elif (choice==2):
                read()
            elif (choice==3):
                update()
            elif (choice==4):
                delete()
            else:
                print('Enter Correct Option')
            userChoice = int(input('Press 0 to Continue the Program or 1 to stop the program: '))
            if (userChoice == 1):
                condition = False 
        except ValueError:
            print("Error!, Entered Value is not Integer")                        