import time
import math

from Data_Storage import *

def populate_database(config):
    #Establishes a connection to the database
    entry = establish_connection(config)
    #Creates a database named TEST_DB for test code
    create_database(entry, "TEST_DB")

    #Appends the database to the dictionary
    config['database'] = 'TEST_DB'

    #Creates 2 tables in the database for storing sensor data
    create_table(entry, "LIGHT_SENSOR")
    create_table(entry, "WATER_SENSOR")

    #Pre-created data to populate the test table for light_sensors
    light_data_one = ['Light_Sensor', 30, "05-12-2017 at 14:15:35"]
    light_data_two = ['Light_Sensor', 35, "07-12-2017 at 08:00:00"]
    light_data_three = ['Light_Sensor', 80, "09-12-2017 at 12:16:45"]
    light_data_four = ['Light_Sensor', 40, "13-12-2017 at 22:19:30"]

    #Pre-created data to populate the test table for water_sensors
    water_data_one = ['Water_Sensor', 1, "07-12-2017 at 08:00:00"]
    water_data_two = ['Water_Sensor', 1, "05-12-2017 at 14:15:35"]
    water_data_three = ['Water_Sensor', 0, "09-12-2017 at 12:16:45"]
    water_data_four = ['Water_Sensor', 0, "13-12-2017 at 22:19:30"]

    #Populating and commiting the database entry for the program.
    add_data(entry, "LIGHT_SENSOR", light_data_one)
    add_data(entry, "LIGHT_SENSOR", light_data_two)
    add_data(entry, "LIGHT_SENSOR", light_data_three)
    add_data(entry, "LIGHT_SENSOR", light_data_four)
    add_data(entry, "WATER_SENSOR", water_data_one)
    add_data(entry, "WATER_SENSOR", water_data_two)
    add_data(entry, "WATER_SENSOR", water_data_three)
    add_data(entry, "WATER_SENSOR", water_data_four)

    #Closes the client access to the database
    entry.close()

def remove_database(config):
    #Establishes a connection to the database
    entry = establish_connection(config)

    #Removes the tables for sensor data
    cursor.execute("DROP TABLE LIGHT_SENSOR")
    cursor.execute("DROP TABLE WATER_SENSOR")

    #Closes the client access to the database
    entry.close()           