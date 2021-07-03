from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
Name: 
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""


def main():
    """
    Karel will check whether the first column needs to be fixed.
    Then, Karel will move forward to check the rest of columns and see if any columns need to be fixed.
    Finally, Karel will move to the end and all columns will be fixed.
    """
    while front_is_clear():
        fixed_column()
        move_forward()
    fixed_column()


def move_forward():
    """
    Kare will move forward 4 times.
    """
    for i in range(4):
        move()


def turn_around():
    """
    Karel will turn upside down by turning left twice.
    """
    for i in range(2):
        turn_left()


def move_to_bottom():
    """
    Pre-condition: Karel is at the top of the column, facing North.
    Post-condition: Karel is at the bottom of the column, facing East.
    """
    turn_around()
    for i in range(4):
        move()
    turn_left()


def fixed_column():
    """
    Pre-condition: Karel is at the bottom of the column, facing East.
    Post-condition: After fixing the column, Karel is at the bottom of the column, facing East.
    """
    turn_left()
    while front_is_clear():
        if not on_beeper():
            put_beeper()
        else:
            move()
    if not on_beeper():
        put_beeper()
    move_to_bottom()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
