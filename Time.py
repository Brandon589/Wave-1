# Units of Time
day = int(input("Enter number of days: "))
hour = int(input("Enter number of hours:"))
minute = int(input("Enter number of minutes: "))
sec = int(input("Enter number of seconds: "))
day_sec = day * 86400
hour_sec = hour * 3600
minute_sec = minute * 60
print("This equals to", day_sec + hour_sec + minute_sec + sec , "seconds")

 #Units of Time (Again)
total_secs = int(input("Enter number of seconds: "))
number_of_days = total_secs // 86400
total_secs = total_secs - number_of_days*24*60*60
number_of_hours = total_secs // 3600
total_secs = total_secs - number_of_hours*60*60
number_of_minutes = total_secs // 60
total_secs = total_secs - number_of_minutes*60
number_of_seconds = total_secs
total_secs = number_of_seconds
print(f"{number_of_days}:{number_of_hours}:{number_of_minutes}:{number_of_seconds}")

# Current Time
import time
x = time.asctime()
print(x)
