### Dates ###

import datetime 

timenow = datetime.datetime.now()

print(timenow.year)
print(timenow.month) 
print(timenow.day)
print(timenow.hour)
print(timenow.minute)
print(timenow.second)
print(timenow.timestamp())


from datetime import datetime

marca_de_tiempo = timenow.timestamp()

print(marca_de_tiempo)

year_2023 = datetime(2023, 1, 1)

def print_date(date):
    print(date.year)
    print(date.month) 
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

print_date(timenow)
print_date(year_2023)

from datetime import time

current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)
print(current_time.min) 

from datetime import date

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date.min) 

current_date = date(2023, 2, 1)

print(current_date.year)
print(current_date.month)
print(current_date.day)


current_date = date(current_date.year + 1, current_date.month + 1, current_date.day) # Para cambiar los datos

print(current_date.year)

from datetime import timedelta

# print(year_2023.date - current_date)

diff = year_2023 - timenow
print(diff)

diff = year_2023.date() - current_date
print(diff)

print(year_2023.time)

time_delta = timedelta()

start_timedelta = timedelta(200, 100, 1000, weeks = 10)
end_timedelta = timedelta(300, 100, 1000, weeks = 13)

print (end_timedelta - start_timedelta)
print (end_timedelta + start_timedelta)