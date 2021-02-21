#!/usr/bin/python
#import mysql.connector
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(user='new',
                             password='pass',
                             database='vaccineCenters',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `vacLocation` (`LocationName`, `Address`, `ZipCode`, `PhoneNumber`               , `VaccineCount`) VALUES (%s,%s,%d,%d,%d);"
       # cursor.execute(sql, ('Dallas County Health and Human Services','2377 N Stemmons Fwy, Dallas, TX 75207','75207','12148192000','21067'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `Id`, `ZipCode` FROM `vacLocation` WHERE `PhoneNumber`=%s"
        cursor.execute(sql, ('12148192000',))
        result = cursor.fetchone()
        print(result)

def db_fun():
    db = mysql.connector.connect(host='127.0.0.1', database='vaccineCenters', user='new')        
    #print("hi2")
    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()
    #print("hi3")
    # Use all the SQL you like
    cur.execute("SELECT * FROM vacLocation")
    #print("hi4")

    # print all the first cell of all the rows
    for row in cur.fetchall():
        print(row[0])

    db.close()
