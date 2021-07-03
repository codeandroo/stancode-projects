"""
File: hailstone.py
Name: Andrew Chao
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    print('This program computes Hailstone sequences.')

    original_number = int(input('Please enter a number: '))
    # The variable, original_number, is used to identify whether the user enters 1

    number = original_number
    # The variable, number, is used to be calculated in the process of Hailstone sequences.

    step = 0
    # The variable, step, is used to record how many steps in the while loop

    while True:
        if number == 1:
            break
        else:
            step += 1
        # When the input number is odd
        if number % 2 == 1:
            print(str(number) + ' is odd, so I make 3n+1: ' + str(3 * number + 1))
            number = 3 * number + 1
        else:
            print(str(number) + ' is even, so I take half: ' + str(int(number / 2)))
            number = int(number / 2)

    if original_number == 1:
        print('It took 0 steps to reach 1.')
    else:
        print('It took ' + str(step) + ' steps to reach 1.')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
