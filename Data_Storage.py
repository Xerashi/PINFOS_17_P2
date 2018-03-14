    #Python script containing methods to interface with a MySQL server

#Importing required base libraries
from __future__ import print_function
from datetime import date, datetime, timedelta
#Dependancy library to access MySQL
import mysql.connector

#Method to open a connection to the database
def establish_connection(config):
    try:
        #Attempts to access the database using our config dictionary.
        entry = mysql.connector.connect(**config)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Access has been denied.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist.")
        else:
            print(err)  
    else:
        entry.close()
    return entry

#Method to create a database
def create_database(entry, DB_NAME):
    cursor = entry.cursor()
    try: 
        cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER 'utf-8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed to create a database.").format(err)
        exit(1)
    cursor.close()

#Method to create a table
def create_table(entry, TABLE_NAME):
    cursor = entry.cursor()
    for TABLE_NAME, ddl in TABLES.iteritems():
        try:
            print("Creating table {}: ".format(TABLE_NAME), end='')
            cursor.execute(ddl)
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
    table_sql = ("INSERT INTO " + TABLE_NAME + " "
                 "(sensor_name, raw_data, time_stamp) "
                 "VALUES (%s, %s, %s)")
    cursor.execute(table_sql, table_data)
    emp_no = cursor.lastrowid
    entry.commit()
    cursor.close()

#Method to query a table for data
def query_data(entry, TABLE_NAME, threshold_one):
    cursor = entry.cursor()

    query = ("SELECT sensor_name, raw_data, time_stamp FROM " + TABLE_NAME + " "
             "WHERE raw_data >= " + threshold_one + " LIMIT 2")

    cursor.execute(query)
    for (sensor_name, raw_data, time_stamp) in cursor:
        print("{} had a value of {} at {:%d %b %Y}.").format(sensor_name, raw_data, time_stamp)
    cursor.close()