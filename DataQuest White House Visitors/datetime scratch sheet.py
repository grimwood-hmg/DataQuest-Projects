#!/usr/bin/env python3
## DataQuest IO
## Python for Data Science: Intermediate
## Working with Dates and Times in Python

# import module with alias dt
import datetime as dt

# instantiate an object repping date 2000-01-01
eg_1 = dt.datetime(2000, 1, 1)
# dt is the alias for module, datetime is the class
print(eg_1)

eg_2 = dt.datetime(1985, 3, 13, 21, 26, 2)
# instantiates an object repping 1985 March 13, 9:26.02 p.m. or 21:26:02
print(eg_2)

# exercise in pt 4

ibm_founded = dt.datetime(1911, 6, 16)
man_on_moon = dt.datetime(1969, 7, 20, 20, 17)
print(ibm_founded)
print(man_on_moon)

# pt 5
# using strptime to parse strings as dates

opened_file = open('.../Files/Python/DataQuest Date and Times - White House visitors/potus_visitors_2015.csv')
from csv import reader
read_file = reader(opened_file)
potus = list(read_file)
potus = potus[1:]
print('\n')
print('*~~~$*$~~~*')
print('\n')
print(len(potus))
print(potus[-1][2])
print('\n')
print('*~~~$*$~~~*')
print('\n')
date_1_str = "24/12/1984"
print(date_1_str)
date_1_str = dt.datetime.strptime(date_1_str, "%d/%m/%Y")
print(type(date_1_str))
# so it was a string, but after line 38, it changed the class
# result: <class 'datetime.datetime'>
print(date_1_str)
print('\n')
print('*~~~$*$~~~*')
print('\n')
print('pt 5 exercise scratch')
date_format = "%m/%d/%y %H:%M"
for i in potus:
	oldy = i[2]
	oldy = dt.datetime.strptime(oldy, date_format)
	i[2] = oldy
	
print('\n')
print('*~~~$*$~~~*')
print('pt 6 scratch: using strftime to format dates')
print('\n')
time_object = dt.datetime(1984, 12, 24)
day = time_object.day
month = time_object.month
year = time_object.year
time_string = "{}/{}/{}".format(day, month, year)
print("The time_object:", time_object)
print("The time_string:", time_string)
timely_object = dt.datetime(1984, 12, 24)
timely_string = timely_object.strftime("%d/%m/%Y")
print(timely_string)
timely_string1 = timely_object.strftime("%B %d, %Y")
print(timely_string1)
timely_string2 = timely_object.strftime("%A, %B %d, %Y at %I:%M %p")
print(timely_string2)

print("pt 6 excercise")
print('\n')
# Make an empty dict
visitors_per_month = {}
for i in potus:
	time_vari = i[2]
	stringy_time = time_vari.strftime("%B, %Y")
	if stringy_time not in visitors_per_month:
		visitors_per_month[stringy_time] = 1
	else:
		visitors_per_month[stringy_time] += 1
print(visitors_per_month)	

print('\n')
print('*~~~$*$~~~*')
print('pt 7 scratch: time class')
print('\n')

appt_times = []

for i in potus:
	timey_wimey = i[2]
	timey_obj = timey_wimey.time()
	appt_times.append(timey_obj)
	
print('\n')
print('*~~~$*$~~~*')
print('pt 8 scratch: comparisons, min max')
print('\n')
	
min_time = min(appt_times)
max_time = max(appt_times)
print("The min time was:", min_time, "And the max time was:", max_time)

print('\n')
print('*~~~$*$~~~*')
print('pt 9 scratch: timedelta')
print('\n')

dt_1 = dt.datetime(1981, 1, 31)
dt_2 = dt.datetime(1984, 6, 28)
dt_3 = dt.datetime(2016, 5, 24)
dt_4 = dt.datetime(2001, 1, 1, 8, 24, 13)

answer_1 = (dt_2 - dt_1)
print(answer_1)

answer_2 = dt_3 + dt.timedelta(days=56)
print(answer_2)

answer_3 = dt_4 - dt.timedelta(seconds=3600)

print('\n')
print('*~~~$*$~~~*')
print('pt 10 scratch: meeting analysis')
print('\n')

date_format = "%m/%d/%y %H:%M"

for e in potus:
	end_date = e[3]
	end_date = dt.datetime.strptime(end_date, date_format)
	e[3] = end_date

appt_lengths = {}

for i in potus:
	startee = i[2]
	endor = i[3]
	length = endor - startee
	if length not in appt_lengths:
		appt_lengths[length] = 1
	if length in appt_lengths:
		appt_lengths[length] += 1
		
min_length = min(appt_lengths)
max_length = max(appt_lengths)

#
#- Explore min-max. Why are these values larger than one might expect
#- Find the visitor who spend the most time at the White House
#- Who visited the most each month?

print("The minimum length of time:", min_length)
print("The maximum length of time:", max_length)

min_max = {}

for i in potus:
	endor = i[3]
	startor = i[2]
	name = i[0]
	length = endor - startor
	if length == min(appt_lengths):
		min_max["minimum"] = name
	elif length == max(appt_lengths):
		min_max["maximum"] = name
		
print(min_max)		