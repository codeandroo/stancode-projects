"""
File: weather_master.py
Name: Andrew Chao
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

EXIT = -1


def main():
	print('stanCode "Weather Master 4.0"!')

	temp = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)?'))

	# Initial values for the Weather Master 4.0
	max_temp = temp
	min_temp = temp
	day = 1
	sum_temp = temp

	# Check whether the first temperature is under 16 degrees
	if temp < 16:
		cold_day = 1
	else:
		cold_day = 0

	if temp == EXIT:
		# Program will stop if the first temperature is equal to EXIT number
		print('No temperatures were entered.')

	else:
		# Allow more temperatures to be entered by users
		while True:
			temp = int(input('Next Temperature: (or' + str(EXIT) + 'to quit)?'))
			if temp == EXIT:
				break
			else:
				# Find the highest temperature
				if temp > max_temp:
					max_temp = temp

				# Find the lowest temperature
				if temp < min_temp:
					min_temp = temp

				# Count days
				day += 1

				# Sum temperatures
				sum_temp += temp

				# Count cold days
				if temp < 16:
					cold_day += 1

		print('Highest temperature = ' + str(max_temp))
		print('Lowest temperature = ' + str(min_temp))
		print('Average = '+str(sum_temp / day))
		print(str(cold_day) + ' cold day(s)')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
