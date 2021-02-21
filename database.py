#!/usr/bin/python
import mysql.connector

def db_fun():
    db = mysql.connector.connect(host='127.0.0.1', database='vaccineCenters', user=root)        
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
