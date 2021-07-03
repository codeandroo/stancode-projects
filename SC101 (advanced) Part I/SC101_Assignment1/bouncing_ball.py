"""
File: bouncing_ball.py
Name: Andrew Chao
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
switch = True
ball = GOval(SIZE, SIZE)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """

    # create a ball at the initial position
    ball.filled = True
    ball.fill_color = 'black'
    window.add(ball, x=START_X, y=START_Y)

    # Click to trigger the animation
    onmouseclicked(ball_dropping)


def ball_dropping(mouse):
    global switch, ball

    # When the user clicks the scope of the screen, it will trigger the animation
    if mouse.x >= 0 and mouse.y >= 0:
        if switch:
            vy = 0

            # Turn off the switch to prevent any click events from happening during the animation
            switch = False

            # Animation
            while True:
                ball.move(VX, vy)
                vy += GRAVITY
                if ball.y >= window.height:
                    vy *= -REDUCE

                # When the ball bounces out of the screen, rest the ball's position and turn on the switch
                elif ball.x >= window.width:
                    window.add(ball, x=START_X, y=START_Y)
                    switch = True
                    break

                pause(DELAY)


if __name__ == "__main__":
    main()
