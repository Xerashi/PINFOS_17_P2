import RPi.GPIO as GPIO
import time

#GPIO Set to PIN numbering system
GPIO.setmode(GPIO.BCM)

#GPIO Water Sensor
GPIO.setup(2, GPIO.IN)

#Method to Cycle Light Sensor
def light_sense():
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
    print("light: " + str(count))

#Method to print the approximate light value to console every 2 seconds
def light_value(attempt):

    #Converts the sensor value, and interation number to strings
    attempt = str(attempt)
    sensor_value = str(GPIO.input(2))

    #If the pin output is set to 1/HIGH it produces the approximate value of the sensor
    if GPIO.input(2) == 1:
        print("Iteration " + attempt + ": " + sensor_value + ".")
        time.sleep(2)

    #If the PIN output is set to 0/LOW it just submits a value of 0 for the sensor    
    else:
        print("Iteration " + attempt + ": " + str(0))
        time.sleep(2)

#Creates a number to establish increments
i = 1

#Loop to run the 2 methods in a cycle
while i > 0:
    light_sense()
    value(i)
    #Increases the increment number
    i += 1