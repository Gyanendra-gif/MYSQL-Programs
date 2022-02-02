"""
@Author: Gyanendra
@Date: 01/01/2022
@Last Modified by: Gyanendra
@Last Modified time: 01/01/2022 
@Title : Joins Programs in Python
"""
import mysql.connector as con

connection = con.connect(host='localhost',database='store',user='root',password='Janu@1252')
cursor= connection.cursor()

def innerJoin():
    """
    Description:
        Function is used to fetch data from the table after inner join from other table 
    Parameter:
        None
    Return:
        None
    """
    sql = "SELECT items.id, customer.name FROM items INNER JOIN customer ON items.id=customer.cid;"
    try:
        cursor.execute(sql)
        data=cursor.fetchall()
        for item in data:
            print(item)
    except Exception as e:
        print(e)

def leftJoin():
    """
    Description:
        Function is used to fetch data from the table after left join from other table 
    Parameter:
        None
    Return:
        None
    """
    sql = "SELECT customer.name, items.id  FROM customer LEFT JOIN items ON customer.cid=items.id ORDER BY customer.name;"
    try:
        cursor.execute(sql)
        data=cursor.fetchall()
        for item in data:
            print(item)
    except Exception as e:
        print(e)    

def rightJoin():
    """
    Description:
        Function is used to fetch data from the table after right join from other table 
    Parameter:
        None
    Return:
        None
    """
    sql = "SELECT items.id, customer.name, customer.city  FROM items RIGHT JOIN customer ON customer.cid=items.id ORDER BY items.id;"
    try:
        cursor.execute(sql)
        data=cursor.fetchall()
        for item in data:
            print(item)
    except Exception as e:
        print(e)

def crossJoin():
    """
    Description:
        Function is used to fetch data from the table after cross join from other table 
    Parameter:
        None
    Return:
        None
    """
    sql = "SELECT customer.name, items.id FROM customer CROSS JOIN items ON items.id=customer.cid;"
    try:
        cursor.execute(sql)
        data=cursor.fetchall()
        for item in data:
            print(item)
    except Exception as e:
        print(e)

def selfJoin():
    """
    Description:
        Function is used to fetch data from the table after self join from other table 
    Parameter:
        None
    Return:
        None
    """
    sql = "SELECT A.name as CustomerName1, B.name as CustomerName2, A.city FROM customer A, customer B WHERE A.cid<>B.cid AND A.city=B.city ORDER BY A.city;"
    try:
        cursor.execute(sql)
        data=cursor.fetchall()
        for item in data:
            print(item)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    condition = True
    while (condition == True):
        try:
            choice = int(input("Enter your choice to perform operation, \n 1)Inner join \n 2)Left join \n 3)Right join \n 4)Cross Join \n 5)Self join:-"))
            if (choice==1):
                innerJoin()
            elif (choice==2):
                leftJoin()
            elif (choice==3):
                rightJoin()
            elif (choice==4):
                crossJoin()
            elif (choice==5):
                selfJoin()
            else:
                print('Enter Correct Option')
            userChoice = int(input('Press 0 to Continue the Program or 1 to stop the program: '))
            if (userChoice == 1):
                condition = False 
        except ValueError:
            print("Error!, Entered Value is not Integer")