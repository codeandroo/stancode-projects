"""
File: rocket.py
Name: Andrew Chao
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant determines rocket size.
SIZE = 3


def main():
    """
    This rocket consist of 6 parts, including 2 heads, 2 belts, 1 upper body and 1 lower body.
    Users are allowed to change the constant, SIZE, to adjust the size of rocket.
    """
    head()
    belt()
    upper()
    lower()
    belt()
    head()


def head():
    """
    In the head function, there are 1 outer for loop and 2 inner for loops.
    The outer one is used to build rows, which can be understood as the height of this element.
    As for the inner ones, the first for loop (j) is used to build the left-half part of each row, while
    the second inner for loop (k) is used to build the mirrored part (right-half).
    """
    for i in range(SIZE):
        # The outer for loop

        print(' ', end='')
        # offset the head to the middle as the belt and body are one space bigger than the head

        for j in range(SIZE):
            # The first inner for loop
            if (i + j) <= SIZE - 2:
                print(' ', end='')
            else:
                print('/', end='')

        for k in range(SIZE):
            # The second inner for loop
            if (i + (SIZE - k - 1)) <= SIZE - 2:
                print(' ', end='')
            else:
                print('\\', end='')
        print('')


def belt():
    """
    In the belt function, there are 2 for loops, using to build the main part of the belt (=).
    Also, in the beginning and the end of the belt, it will put '+' as the boundary of both sides.
    """
    print('+', end='')
    for i in range(SIZE):
        print('=', end='')
    for k in range(SIZE):
        print('=', end='')
    print('+')


def upper():
    """
    In the upper function, there are 1 outer for loop and 2 inner for loops.
    The outer one is used to build rows, which can be understood as the height of this element.
    In terms of the inner ones, the first for loop (j) is used to build the left-half part of each row, while
    the second inner for loop (k) is used to build the mirrored part (right-half).
    """
    for i in range(SIZE):
        # The outer for loop

        for j in range(SIZE+1):
            # The first inner for loop

            if j == 0:
                print('|', end='')
            elif (i + j) < SIZE:
                print('.', end='')
            else:
                if SIZE % 2 == 1:
                    if (i + j) % 2 == 1:
                        print('/', end='')
                    else:
                        print('\\', end='')
                else:
                    if (i + j) % 2 == 0:
                        print('/', end='')
                    else:
                        print('\\', end='')

        for k in range(SIZE+1):
            # The second inner for loop

            if (SIZE - k) == 0:
                print('|', end='')
            elif (i + (SIZE - k)) < SIZE:
                print('.', end='')
            else:
                if SIZE % 2 == 1:
                    if (i + (SIZE - k)) % 2 == 1:
                        print('\\', end='')
                    else:
                        print('/', end='')
                else:
                    if (i + (SIZE - k)) % 2 == 0:
                        print('\\', end='')
                    else:
                        print('/', end='')
        print('')


def lower():
    """
    In the lower function, there are 1 outer for loop and 2 inner for loops.
    The outer one is used to build rows, which can be understood as the height of this element.
    In terms of the inner ones, the first for loop (j) is used to build the left-half part of each row, while
    the second inner for loop (k) is used to build the mirrored part (right-half).
    """
    for i in range(SIZE):
        # The outer for loop

        for j in range(SIZE + 1):
            # The first inner for loop

            if j == 0:
                print('|', end='')
            elif ((SIZE - i - 1) + j) < SIZE:
                print('.', end='')
            else:
                if SIZE % 2 == 0:
                    if ((SIZE - i - 1) + j) % 2 == 1:
                        print('/', end='')
                    else:
                        print('\\', end='')
                else:
                    if ((SIZE - i - 1) + j) % 2 == 0:
                        print('/', end='')
                    else:
                        print('\\', end='')

        for k in range(SIZE + 1):
            # The second inner for loop

            if (SIZE - k) == 0:
                print('|', end='')
            elif ((SIZE - i - 1) + (SIZE - k)) < SIZE:
                print('.', end='')
            else:
                if SIZE % 2 == 0:
                    if ((SIZE - i - 1) + (SIZE - k)) % 2 == 1:
                        print('\\', end='')
                    else:
                        print('/', end='')
                else:
                    if ((SIZE - i - 1) + (SIZE - k)) % 2 == 0:
                        print('\\', end='')
                    else:
                        print('/', end='')
        print('')


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
