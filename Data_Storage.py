#Python script containing methods to interface with a MySQL server
from __future__ import print_function
from datetime import date, datetime, timedelta
import time
#Dependancy library to access MySQL
import mysql.connector
from mysql.connector import errorcode

#Method to open a connection to the database
def establish_connection():   
    entry = mysql.connector.connect(user='root', password='password', host='localhost', db='TEST_DB')
    return entry

#Method to create a database
def create_database(entry, DB_NAME):
    cursor = entry.cursor()
    try: 
        cursor.execute("CREATE DATABASE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Already Exists.")
    cursor.close()

#Method to create a table
def create_table(entry, table_name):
    cursor = entry.cursor()
    try:
        cursor.execute("CREATE TABLE {}(sensor_name VARCHAR(20), raw_data INT(20), time_stamp VARCHAR(50));".format(table_name))
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")
    cursor.close()

#Method to add data to a table
def add_data(entry, TABLE_NAME, table_data):
    cursor = entry.cursor()
    table_sql = ("INSERT INTO " + TABLE_NAME +
                " (sensor_name, raw_data, time_stamp) " 
                "VALUES (%s, %s, %s)")
    cursor.execute(table_sql, table_data)
    emp_no = cursor.lastrowid
    entry.commit()
    cursor.close()

#Method to query a table for data
def query_data(entry, TABLE_NAME, threshold_one):
    cursor = entry.cursor()

    query = ("SELECT sensor_name, raw_data, time_stamp FROM " + TABLE_NAME + " "
            "WHERE raw_data >= " + str(threshold_one) + "  ORDER BY time_stamp ASC LIMIT 2")

    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return data