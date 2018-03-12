#File used to store logical and numerical opperations.
import time
import datetime
import math

def convert_to_seconds(date_input):
    #Cuts off the date from the time
    time_split = date_input[14:]
    #Converts the hours into seconds
    hours = int(time_split[:2]) * 3600
    #Converts the minutes into seconds
    minutes = int(time_split[3:5]) * 60
    #Combines all of the seconds into one integer
    time_split = int(time_split[6:8]) + hours + minutes
    return time_split

def convert_date_to_array(date_input):
    #Cuts off the time from the date
    date_split = date_input
    #Cuts off the days from the input
    days = date_split[0:2]
    #Cuts off the months from the input
    months = date_split[3:5]
    #Cuts off the years from the input
    years = date_split[6:10]
    #Sets an easy to manipulate array
    date_array = [days, months, years]
    return date_array

def compare_date(date_current, date_other):
    date_now = date_current
    date_then = date_other
    years = int(date_now[2]) - int(date_then[2])
    months = int(date_now[1]) - int(date_then[1])
    days = int(date_now[0]) - int(date_then[0])
    date_array = [days, months, years]
    return date_array

def convert_to_readable(value_array):
    time = value_array[3]
    days = value_array[0]
    months = value_array[1]
    years = value_array[2]
    if time < 0:
        time = 86400 + time
        days = days - 1
    if days < 0: 
        days = 30 + days
        months = months - 1
    if months < 0:
        months = 12 + months
        years = years - 1
    new_array = [int(time), int(days), int(months), int(years)]
    return new_array

def readable(positive_array, date_other):
    timer = positive_array[0]
    time_text = convert_time(timer)
    sentance = (date_other + " was: " + str(positive_array[2]) + " months, " + str(positive_array[1]) +" days," + time_text)
    return sentance

def convert_time(timer):
    hours = math.floor(timer/3600)
    timer = timer - (hours * 3600)
    minutes = math.floor(timer/60)
    timer = timer - (minutes * 60)
    result = " {} hours, {} minutes, {} seconds ago.".format(hours, minutes, timer)
    return result

def get_interval(date_time_current, date_time_other):
    date_current = convert_date_to_array(date_time_current)
    date_other = convert_date_to_array(date_time_other)
    
    date_difference = compare_date(date_current, date_other)

    time_current = convert_to_seconds(date_time_current)
    time_other = convert_to_seconds(date_time_other)
    time_difference = time_current - time_other

    result_array = date_difference
    result_array.append(time_difference)
    print(result_array)
    positive_array = convert_to_readable(result_array)
    print(positive_array)
    result_text = readable(positive_array, date_time_other)
    print(result_text)


#Sets date and time to an easier to store scale.
minimized_time = time.strftime('%H:%M:%S')
minimized_date = time.strftime('%d-%m-%Y')
current_date = minimized_date + " at " + minimized_time
other_date = "05-12-2017 at 14:15:35"
get_interval(current_date, other_date)