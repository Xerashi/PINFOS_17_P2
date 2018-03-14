#Requirements to run Testing.py to properly log the results
# 1. Valid installation of MySQL
# 2. Path access to Python3 as Python
# 3. Properly installed mysql-connector library 

import RPi.GPIO as GPIO
import time
import math

from Sensor_Data import *
from Display_Structure import *
from Data_Storage import *
from Operations import *
from State_Logic import *
from Database_Generator import *

#Main loop logic for testing information
config_true = {
    'username' : 'admin',
    'password' : 'password',
}

config_false = {
    'username' : 'name',
    'password' : 'pass',
}

#Error testing an error with login response
if establish_connection(config_false) == error:
    print("Status: Okay")
else:
    print("Status: Error")

#Error testing an expected true login response    
if establish_connection(config_true) == fact:
    print("Status: Okay")
else:
    print("Status: Error")

#Uses the generate_database method in Database_Generator.py to create a test database.
generate_database(config_true)

#To implement: 
# 1. Database queries for information handling to view non-negative timescales.
# 2. State handling and proper returned value based off spoofed data.
# 3. Testing 2 dates for proper timescale difference
# 4. Creating log file generation for testing, with reasonably written responses.
# 5. Checking the database storage and query for a distinct piece of data.
# 6. Checking the sensor cycling returns proper values.
# 7. Checks the logic which dictates state generation, and the accuracy of the result.