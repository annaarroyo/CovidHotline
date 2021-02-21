#!/usr/bin/python
import mysql.connector

def db_fun():
    db = mysql.connector.connect(host="localhost",    # your host, usually localhost
                        user="angel",        # your username, 
                        database="vaccineCenters",  # name of the data base
                        port=3306)        
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
