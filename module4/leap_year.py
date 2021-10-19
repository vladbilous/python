while True:
	response = (input('Do you want to enter the range? (Y/N) '))
	# If a user wants to see all leap years within the range
	if response == 'Y':
		start_year = int(input('Enter the start year: '))
		end_year = int(input('Enter the end year: '))
		# Checking all years within the range
		for year in range(start_year, end_year + 1):
			if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
				print('Leap year is: {}'.format(year))
		break
	else:
		year = int(input('Enter the year to check: '))
		# if year divides to 4 and (100 or 400) without remaining it's a leap year
		if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
			print('It is a leap year! 366 days in a year!\n')
		else:
			print('It is not a leap year! 365 days in a year!\n')
			# Check close years is they are leap.
			for item in (year + 1, year -1, year + 2, year - 2, year + 3, year -3 ):
				if (item % 4 == 0) and (item % 100 != 0) or (item % 400 == 0):
					print ('The closest leap year is: {}'.format(item))
					break
	break

input()

