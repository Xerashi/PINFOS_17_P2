import RPi.GPIO as GPIO
import time
import math

from Sensor_Data import *
from Display_Structure import *
from Data_Storage import *
from Operations import *
from State_Logic import *

#Creates a method to validate the state depending on the sensor data
def state_check(light_sensor, water_sensor, config):
    #Initializes the state value as 0
    state = 0

    #Connects to mySQL server
    entry = establish_connection(config)
    
    if light_sensor >= 80:
        state = state + 1
        light_data = query_data(entry, "LIGHT_SENSOR")
            state = state + 1
            
    if water_sensor == 0:
        state = state + 1
        light_data = query_data(entry, "WATER_SENSOR")
            state = state + 1

    return state
