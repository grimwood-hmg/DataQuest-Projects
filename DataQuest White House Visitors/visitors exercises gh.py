#!/usr/bin/env python3
## DataQuest IO
## Python for Data Science: Intermediate
## Working with Dates and Times in Python

#Pt 1: Intro
# open the file

opened_file = open('.../Files/Python/DataQuest Date and Times - White House visitors/potus_visitors_2015.csv')
from csv import reader
read_file = reader(opened_file)
potus = list(read_file)
potus = potus[1:]

#pt 4 importing date time

import datetime as dt

# pt 5 using strptime

appt_start_date_format = "%m/%d/%y %H:%M"
for i in potus:
	start_date = i[2]
	start_date = dt.datetime.strptime(start_date, appt_start_date_format)
	i[2] = start_date
	
#pt 6 exercise using strftime to create freq table for monthly visitors
	
visitors_per_month = {}
for i in potus:
	time_vari = i[2]
	stringy_time = time_vari.strftime("%B, %Y")
	if stringy_time not in visitors_per_month:
		visitors_per_month[stringy_time] = 1
	else:
		visitors_per_month[stringy_time] += 1

#pt 7 time class exercise: create list of appt times
		
appt_times = []

for i in potus:
	timey_wimey = i[2]
	timey_obj = timey_wimey.time()
	appt_times.append(timey_obj)

#pt 8 comparing time obj: calc min/max times for meeting appt starts

min_time = min(appt_times)
max_time = max(appt_times)

#pt 10 summarizing appointment lengths

end_date_format = "%m/%d/%y %H:%M"
for e in potus:
	end_date = e[3]
	end_date = dt.datetime.strptime(end_date, end_date_format)
	e[3] = end_date
	
appt_lengths = {}

for i in potus:
	startee = i[2]
	endor = i[3]
	length = endor - startee
	if length not in appt_lengths:
		appt_lengths[length] = 1
	else:
		appt_lengths[length] += 1
		
min_length = min(appt_lengths)
max_length = max(appt_lengths)

