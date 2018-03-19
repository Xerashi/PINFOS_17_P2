#Requirements to run Testing.py to properly log the results
# 1. Valid installation of MySQL
# 2. Path access to Python3 as Python
# 3. Properly installed mysql-connector library 
import time
import math
import mysql.connector

from Database_Generator import populate_database, remove_database
from Data_Storage import *
from Operations import *

#Main loop logic for testing information
config = {
    'user':'root',
    'password':'password',
}

config_false = {
    'user' : 'name',
    'password' : 'pass',
    'host' : '127.0.0.1',
}


entry = establish_connection()
print(entry)
#Appends the database to the dictionary
config['database'] = 'TEST_DB'
#Uses the generate_database method in Database_Generator.py to create a test database.
populate_database(entry)

entry = establish_connection()
light_data = query_data(entry, 'LIGHT_SENSOR', 40)
water_data = query_data(entry, 'WATER_SENSOR', 1)

for i in light_data:
    print(i)
for i in water_data:
    print(i)

get_interval(light_data[1][2], light_data[0][2])
get_interval(water_data[0][2], water_data[1][2])
#To implement: 
# 1. Database queries for information handling to view non-negative timescales.
# 2. State handling and proper returned value based off spoofed data.
# 3. Testing 2 dates for proper timescale difference
# 4. Creating log file generation for testing, with reasonably written responses.
# 5. Checking the database storage and query for a distinct piece of data.
# 6. Checking the sensor cycling returns proper values.
# 7. Checks the logic which dictates state generation, and the accuracy of the result.