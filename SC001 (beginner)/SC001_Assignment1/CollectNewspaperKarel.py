from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
Name: 
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    """
    At first, Karel faces East.
    Next, Karel will move outside of the door to pick up the newspaper (aka. beeper).
    Then, Karel will come back to the original place and read the newspaper (put down the beeper),
    facing East.
    """
    move_outside()
    carry_newspaper_and_move_back()


def carry_newspaper_and_move_back():
    """
    Pre-condition: Karel is facing West on the beeper that is located at the Street 3, Avenue 6.
    Post-condition: Karel is on Street 4, Avenue 3, facing East and standing on the beeper.
    """
    pick_beeper()
    for i in range(3):
        move()
    turn_right()
    move()
    turn_right()
    put_beeper()


def turn_right():
    """
    Karel will turn right by turning left 3 times.
    """
    for i in range(3):
        turn_left()


def turn_around():
    """
    Karel will turn upside down by turning left twice.
    """
    for i in range(2):
        turn_left()


def move_outside():
    """
    Pre-condition: Karel is at the Street 4, Avenue 3, facing East.
    Post-condition: Karel is at the Street 3, Avenue 6, facing West.
    """
    for i in range(2):
        move()
    turn_right()
    move()
    turn_left()
    move()
    turn_around()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
