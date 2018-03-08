#Core Python Program File, contains all external resource imports, and the navigation between them.
#Basic library imports
import RPi.GPIO as GPIO
import time

#Other scripts in the directory
from Sensor_Data import *
from Display_Structure import *
from Data_Storage import *
from Operations import *

#Creates a dictonary of the database login
config = {
    'user' : 'admin',
    'password' : 'Pinfos17',
    'host' : '127.0.0.1',
    }

def __init__(self):
    #Sets date and time to an easier to store scale.
    minimized_time = time.strftime('%H:%M:%S')
    minimized_date = time.strftime('%d-%m-%Y')
    current_date = minimized_date + " at " + minimized_time

    #Method to convert the date into a readable integer.
    time_seconds = convert_to_seconds(current_date)

    #Run first itteration of sensor data
    cycle_sensors()

    #Creates data-arrays for the light and water sensor
    light_data = {"Light Sensor", str(light_value()), current_date}
    water_data = {"Water Sensor", str(GPIO.input(3)), current_date}

    #Checks which face the LCD should be displaying
    state = state_check(light_data[1], water_data[1])

    #Pushes the correct state to the screen
    modify_display(state)

    #Connects to mySQL server
    entry = establish_connection(config)
  
    #Creates a database called SENSOR_DATA, and two tables called LIGHT_SENSOR and WATER_SENSOR
    create_database(entry, "SENSOR_DATA")
    create_table(entry, "LIGHT_SENSOR") 
    create_table(entry, "WATER_SENSOR")

    #Adds the data for each sensor to their respective tables
    add_data(entry, "LIGHT_SENSOR", light_data)
    add_data(entry, "WATER_SENSOR", water_data)

    #Takes a 10 minute break from calculating
    time.sleep(600)

