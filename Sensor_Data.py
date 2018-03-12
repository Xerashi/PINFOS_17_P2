import RPi.GPIO as GPIO
import time
import * from Data_Storage

#GPIO Set to PIN numbering system
GPIO.setmode(GPIO.BCM)

#GPIO Water Sensor
GPIO.setup(2, GPIO.IN)

#Method to Cycle Light Sensor
def light_cycle():
    #Resets the counter for every itteration
    count = 0

    #Reset's the PIN on slot 3
    GPIO.setup(3, GPIO.OUT)
    GPIO.output(3, GPIO.LOW)

    #Stops the program for 0.1 seconds
    time.sleep(0.1)

    #Initializes the GPIO PIN as input
    GPIO.setup(3, GPIO.IN)

    #Creates an incremental loop to detect while the light isn't full power, it counts up approximately 1 second
    while GPIO.input(3) == GPIO.LOW:
        count += 1
    return count

#Method to print the approximate light value to console every 2 seconds
def sensor_value(sensor_name, value):
    #Converts the sensor value, and interation number to strings
    sensor_value = value

    #Prints out the sensor name and value based on whats passed into the method
    if sensor_name != null && sensor_value != null:
        print(sensor_name + ": " + sensor_value + ".")
        time.sleep(2)
    else:
        print("Missing Sensor Values.")

#Method to cycle both sensors counts and values
def cycle_sensors():
    light_var = str(light_cycle())
    water_var = str(GPIO.input(2))
    sensor_value("Light", light_var)
    sensor_value("Water", water_var)