#Day16_exercise

from datetime import datetime,time,date
#Get the current day, month, year, hour, minute and timestamp from datetime module
now=datetime.now()
print(now)
day=now.day
print(day)
month=now.month
print(month)
year=now.year
print(year)
hour=now.hour
print(hour)
minute=now.minute
print(minute)
second=now.second
print(second)
microsecond=now.microsecond
print(microsecond)
timestamp=now.timestamp()
print(timestamp)

#Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
frmt_date=now.strftime("%m/%d/%Y, %H:%M:%S")
print(frmt_date)

#Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
print("date_string =", date_string)
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

#Calculate the time difference between now and new year.
t1=date(year=2025, month=4, day=11)
t2 = date(year=2026, month=1, day=1)
time_diff=t1-t2
print(time_diff)

#Calculate the time difference between 1 January 1970 and now.
t1=date(year=2025, month=4, day=11)
t2 = date(year=1970, month=1, day=1)
time_diff=t1-t2
print(time_diff)

