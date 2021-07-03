from karel.stanfordkarel import *

"""
File: MidpointKarel.py
Name: 
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    Check whether Karel is in a 1x1 world or not.
    If not, Karel will proceed with functions that can help Karel to find the midpoint.
    Firstly, Karel will use beepers as new boundaries on two sides of street 1.
    Then, Karel will move between boundaries and the distance between boundaries will become smaller.
    Finally, when the boundaries narrow down to the midpoint, Karel will offset her position to the midpoint.
    """
    if front_is_clear():
        beeper_boundary()
        put_beeper_to_the_midpoint()
        offset_position_to_the_midpoint()
    else:
        # When Karel is in the 1x1 world, which is kind of exception of other worlds, she only needs to put a beeper
        put_beeper()


def offset_position_to_the_midpoint():
    """
    Pre-condition:
    Post-condition:
    """
    turn_left()
    if front_is_clear():
        move()
        if not on_beeper():
            turn_around()
            for i in range(2):
                move()
    else:
        pick_beeper()
        turn_left()
        move()


def put_beeper_to_the_midpoint():
    """
    Pre-condition: Karel is standing on a position without beepers, facing East or facing West.
    Post-condition: Karel will move to the other side, pick up the beeper (as boundary) and
                    put a new beeper next to the original one. (the side that closes to the midpoint)
    While repeating this process again and again, Karel can move to the midpoint.
    """
    while front_is_clear():
        if not on_beeper():
            if not facing_north():
                # the condition of not facing_north is used to make both facing East and facing West work
                move_to_the_beeper()
                pick_beeper()
                move()
                put_beeper()
                move()
            else:
                turn_around()
        else:
            turn_right()
            # turning right is used to break the while loop of front_is_clear
            pick_beeper()
            # picking up the last


def beeper_boundary():
    """
    Pre-condition: Karel is at Street 1, Avenue 1, facing East.
    Post-condition: Karel will be one space away from the right wall, facing West.
                    Also, there is a beeper beside the right and the left wall.
    """
    put_beeper()
    move_to_the_end()
    turn_around()
    put_beeper()
    move()


def turn_right():
    """
    Karel will turn right by turning left 3 times.
    """
    for i in range(3):
        turn_left()


def move_to_the_beeper():
    """
    Pre-condition: Karel is standing on a position without beepers, facing East or facing West.
    Post-condition: Karel will move the other side, stand on a beeper and turn around.
    """
    move()
    while not on_beeper():
        move()
    turn_around()


def turn_around():
    """
    Karel will turn upside down by turning left twice.
    """
    for i in range(2):
        turn_left()


def move_to_the_end():
    """
    Pre-condition: Karel is at Street 1, Avenue 1, facing East.
    Post-condition: Karel will be beside the right wall, facing East.
    """
    while front_is_clear():
        move()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
