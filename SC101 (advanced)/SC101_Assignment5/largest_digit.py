"""
File: largest_digit.py
Name:
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: int, input an integer number
	:return: int, return the biggest digit in n
	"""
	# Convert the negative number to the positive one
	if n < 0:
		n = n - 2 * n
	count = 1  # An initial value to count how many digits in a given number
	length_n = get_digit_number(n, count)
	initial_digit = 0
	ans = largest_digit_helper(n, initial_digit, length_n)
	return ans


def largest_digit_helper(current_n, initial_digit, length_n):
	"""
	:param current_n: int, input an integer number
	:param initial_digit: int, it's a variable used to store the first digit of current_n
	:param length_n: int, it's a variable used to store how many digits in current_n
	:return: int, return the biggest digit in current_n
	"""
	# Base case: when current_n has been split into single digit, the helper function will reach base case
	if length_n == 1:
		if current_n > initial_digit:
			return current_n
		else:
			return initial_digit
	else:
		initial_digit = current_n // 10 ** (length_n - 1)  # Get first digit of current_n
		current_n = current_n % 10 ** (length_n - 1)  # Get the rest digits of current_n
		current_n = largest_digit_helper(current_n, initial_digit, length_n - 1)  # Replace the current_n with the value returned by the base case
		if current_n > initial_digit:
			return current_n
		else:
			return initial_digit


def get_digit_number(n, count):
	"""
	:param n: int, input a positive integer number
	:param count: int, input a initial number (usually 1) to count how many digits in a given number (n)
	:return: int, return a number that represents the number of digit in n
	"""
	if n < 10:
		return count
	else:
		n /= 10
		count += 1
		count = get_digit_number(n, count)
		return count


if __name__ == '__main__':
	main()
