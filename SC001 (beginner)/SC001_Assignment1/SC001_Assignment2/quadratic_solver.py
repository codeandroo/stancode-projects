"""
File: quadratic_solver.py
Name: Andrew Chao
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
    print('This is the stanCode Quadratic Solver! Please enter 3 numbers.')
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))
    if a != 0:
        # If input number is not 0, the program will check how many roots.

        if b * b - 4 * a * c > 0:
            # 2-roots scenario
            print('Two roots: ' + str((-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)) + ' , ' + str(
                (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)))

        elif b * b - 4 * a * c == 0:
            # 1-root scenario
            print('One root: ' + str(-b / (2 * a)))

        else:
            # no-root scenario
            print('No real roots')
    else:
        # If input number is 0, send a warning message to users
        print('The parameter a can not be zero. Please restart the program!')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
