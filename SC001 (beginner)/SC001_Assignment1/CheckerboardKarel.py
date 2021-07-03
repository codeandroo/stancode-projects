from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
Name: 
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""


def main():
    """
    When Karel does not touch the wall, she will move forward and put beepers in a way that beepers
    have one space between each other.
    --> function: draw_row()

    When Karel touches the wall, she will turn change her position to the next row.
    --> function: change_row()

    Finally, Karel will put beepers to the world and each beeper will have one space away from each other.
    """
    if front_is_clear():
        while front_is_clear():
            draw_row()
            change_row()
    else:
        put_beeper()
        turn_left()
        while front_is_clear():
            if on_beeper():
                move()
            else:
                move()
                put_beeper()


def turn_right():
    """
    Karel will turn right by turning left 3 times.
    """
    for i in range(3):
        turn_left()


def change_row():
    """
    Each time when Karel is moving to the end:
        Scenario 1: When Karel is facing East, standing on a beeper and there is no wall on her left-hand side,
                    she will turn left to the next column. Then, Karel will continue to turn left and move 1 step.

        Scenario 2: When Karel is facing East, not standing on a beeper and there is no wall on her left-hand side,
                    she will turn left to the next column. Then, Karel will continue to turn left without moving.

        Scenario 3: When Karel is not facing East, standing on a beeper and there is no wall on her right-hand side,
                    she will turn right to the next column. Then, Karel will continue to turn right and move 1 step.

        Scenario 4: When Karel is not facing East, not standing on a beeper and there is no wall on her right-hand side,
                    she will turn right to the next column. Then, Karel will continue to turn right without moving.

    """
    if facing_east():
        if left_is_clear():
            if on_beeper():
                turn_left()
                move()
                turn_left()
                move()
            else:
                turn_left()
                move()
                turn_left()
    else:
        if right_is_clear():
            if on_beeper():
                turn_right()
                move()
                turn_right()
                move()
            else:
                turn_right()
                move()
                turn_right()


def draw_row():
    """
    Pre-condition: Karel is at Street 1, Avenue 1, facing East.
    Post-condition: Karel is at Street 1, Avenue1, on the beeper and facing West.
    """
    while front_is_clear():
        if not on_beeper():
            put_beeper()
        else:
            move()
            if front_is_clear():
                if not on_beeper():
                    move()
                    if not on_beeper():
                        put_beeper()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)