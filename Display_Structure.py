#Python module for LCD Display
#Requires Pip installed, and RPLCD

#The library for Raspberry Pi LCD interaction.
from RPLCD import CharLCD
#The name of the file with Database access.
import DataStore

#Generic imports
import time

#Creates a dictonary of the database login
config = {
    'user' : 'user',
    'password' : 'password',
    'host' : '127.0.0.1',
    'database' : 'SENSOR_DATA',
    }

#Pin data for the LCD connections
pins_data = [D0, D1, D2, D3, D4, D5, D6, D7] #Only use [D0, D1, D2, D3] for a 4-bit set-up.
pin_rs = R0
pin_e = E0

#Code to initialize the LCD.
lcd = CharLCD(cols = 16, rows = 2, pin_rs, pin_e, pins_data)

#Changes the cursor position and turns it off
lcd.cursor_pos = (1,3)
lcd.cursor_mode = CursorMode.hide

#Writes 'Hello World' to the LCD screen.
lcd.write_string(u'Hello World')

#Two second timeout, followed by a screen clear.
time.sleep(2)
lcd.clear()

#Initializing a database connection
entry = establish_connection(config)

#Executing the method to create a database named "SENSOR_DATA"
try: 
    entry.database = "SENSOR_DATA"
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(cursor)
        entry.database = "SENSOR_DATA"
    else: 
        print(err)
        exit(1)

#Closes the connection
entry.close()
