January = {'abbr':'jan', 'n_days': 31, 'no.': 1, 'full_name': 'January'}
February = {'abbr':'feb', 'n_days': 28, 'no.': 2, 'full_name': 'February'}
March = {'abbr': 'mar', 'n_days': 31, 'no.': 3, 'full_name': 'March'}
April = {'abbr': 'apr', 'n_days': 30, 'no.': 4, 'full_name': 'April'}
May = {'abbr': 'may', 'n_days': 31, 'no.': 5, 'full_name': 'May'}
June = {'abbr': 'jun', 'n_days': 30, 'no.': 6, 'full_name': 'June'}
July = {'abbr': 'jul', 'n_days': 31, 'no.': 7, 'full_name': 'July'}
August = {'abbr': 'aug', 'n_days': 31, 'no.': 8, 'full_name': 'August'}
September = {'abbr': 'sep', 'n_days': 30, 'no.': 9, 'full_name': 'September'}
October = {'abbr': 'oct', 'n_days': 31, 'no.': 10, 'full_name': 'October'}
November = {'abbr': 'nov', 'n_days': 30, 'no.': 11, 'full_name': 'November'}
December = {'abbr': 'dec', 'n_days': 31, 'no.': 12, 'full_name': 'December'}
February_2 = {'abbr': 'feb', 'n_days': 29, 'no.': 2, 'full_name': 'February'}

months_c = [January, February, March, April, May, June, July, August, September, October, November, December]
months_l = [January, February_2, March, April, May, June, July, August, September, October, November, December]

#! Input parameters
date_1 = '20190910'
date_2 = '20210927'
#? Input parameters

def format_change(date):
	part_1 = int(date[:4])
	part_2 = int(date[4:6])
	part_3 = int(date[6:])
	datelist = [part_1, part_2, part_3]

	return datelist

#Receive a year in 4 digits
def common_leap(year):
	if year % 100 == 0:
		if year % 400 == 0:
			tag = 'leap'
		else:
			tag = 'common'
	elif year % 4 == 0:
		tag = 'leap'
	else:
		tag = 'common'
	return tag

#Receive a date (list); Return the number of a day in the year
def get_days(date):
	tag = common_leap(date[0])
	days = 0
	previous_month = date[1]-1
	if tag == 'common':
		for i in months_c[:previous_month]:
			days += i['n_days']
	elif tag == 'leap':
		for i in months_l[:previous_month]:
			days += i['n_days']
	days += date[2]

	return days



#Receive a date (list); Return the number of days between the date and the start of the year
def calculate_days(date_1, date_2):
	no_date_1 = get_days(date_1)
	no_date_2 = get_days(date_2)

	number_of_years = date_2[0] - date_1[0]
	years = []
	for i in range(number_of_years):
		years.append(date_1[0]+i)
	counter = 0
	for i in years:
		if common_leap(i) == 'leap':
			counter += 1
	ydays = number_of_years * 365 + counter

	days = no_date_2 + ydays - no_date_1

	return days

signal_1 = False
signal_2 = True
signal_3 = False
signal_4 = True
signal_5 = False
dates = [date_1, date_2]
names = ['starting', 'ending']
counter = 0

for i in range(len(dates)):
	if len(dates[i]) != 8:
		print("The date_" + str(i+1) + " must have exactly 8 digits! ")
	else:
		counter += 1
	if counter == 2:
		signal_1 = True

while signal_1:
	dates.sort()
	for i in range(len(dates)):
		if int(dates[i][4:6]) > 12 or int(dates[i][4:6]) < 1:
			print("The " + names[i] + " month information is wrong, which cannot be " + dates[i][4:6] + "! ")
			signal_2 = False
		else:
			signal_3 = True
	break

while signal_2:
	while signal_3:
		formatted_dates = []     #For signal_5 part
		for i in range(len(dates)):
			j = format_change(dates[i])
			formatted_dates.append(j)     #For signal_5 part
			tag = common_leap(j[0])
			month_no = j[1] - 1
			if tag == 'common':
				months = months_c
			elif tag == 'leap':
				months = months_l
			if j[2] > months[month_no]['n_days']:
				if j[1] == 2:
					if int(dates[i][6:]) > 29 and tag == 'leap':
						print("Though we know " + str(j[0]) + " is a leap year, but there is just one day more than common years. The February here has 29 days at most! ")
					else:
						print("For " + dates[i] + ", there is only " + str(months[month_no]['n_days']) + " days in " + str(j[0]) + "'s " + str(months[month_no]['full_name']) + "! ")
				else:
					print("For " + dates[i] + ", there is only " + str(months[month_no]['n_days']) + " days in " + str(months[month_no]['full_name']) + "s! ")
				signal_4 = False
			elif j[2] < 1:
				print("For " + dates[i] + ", a month cannot have " + str(j[2]) + " days! ")
				signal_4 = False
			else:
				signal_5 = True
		break
	break

while signal_4:
	while signal_5:
		#start_date = format_change(dates[0])
		#end_date = format_change(dates[1])     #Fulfilled in signal_3
		start_date = formatted_dates[0]
		end_date = formatted_dates[1]
		interval = calculate_days(start_date, end_date)
		print(interval)
		break
	break
