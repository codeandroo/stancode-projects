"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5  # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40  # Height of a brick (in pixels).
BRICK_HEIGHT = 15  # Height of a brick (in pixels).
BRICK_ROWS = 10  # Number of rows of bricks.
BRICK_COLS = 10  # Number of columns of bricks.
BRICK_OFFSET = 50  # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10  # Radius of the ball (in pixels).
BALL_COLOR = '#D46C4E'  # Color of the ball
PADDLE_WIDTH = 75  # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15  # Height of the paddle (in pixels).
PADDLE_OFFSET = 50  # Vertical offset of the paddle from the window bottom (in pixels).
PADDLE_COLOR = '#015C92'  # Color of the paddle

INITIAL_Y_SPEED = 5  # Initial vertical speed for the ball.
MAX_X_SPEED = 3  # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a paddle
        self._paddle = GRect(PADDLE_WIDTH, PADDLE_HEIGHT)
        self._paddle.filled = True
        self._paddle.color = PADDLE_COLOR
        self._paddle.fill_color = PADDLE_COLOR
        self.window.add(self._paddle, x=(self.window_width - PADDLE_WIDTH) / 2, y=self.window_height - PADDLE_OFFSET)

        # Center a filled ball in the graphical window
        self._ball = GOval(BALL_RADIUS * 2, BALL_RADIUS * 2)
        self._ball.filled = True
        self._ball.color = BALL_COLOR
        self._ball.fill_color = BALL_COLOR
        self.window.add(self._ball, x=self.window_width / 2 - BALL_RADIUS, y=self.window_height / 2 - BALL_RADIUS)

        # Default initial velocity for the ball
        self._dx = random.randint(0, MAX_X_SPEED)
        if random.random() > 0.5:
            self._dx = -self._dx
        self._dy = INITIAL_Y_SPEED

        # Draw bricks
        for x in range(0, (BRICK_WIDTH + BRICK_SPACING) * BRICK_COLS, BRICK_WIDTH + BRICK_SPACING):
            for y in range(0, (BRICK_HEIGHT + BRICK_SPACING) * BRICK_ROWS, BRICK_HEIGHT + BRICK_SPACING):
                brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                brick.filled = True
                if y / (BRICK_HEIGHT + BRICK_SPACING) <= 1:
                    brick.color = '#C6A477'
                    brick.fill_color = '#C6A477'
                elif 1 < y / (BRICK_HEIGHT + BRICK_SPACING) <= 3:
                    brick.color = '#ECD59F'
                    brick.fill_color = '#ECD59F'
                elif 3 < y / (BRICK_HEIGHT + BRICK_SPACING) <= 5:
                    brick.color = '#D3E7EE'
                    brick.fill_color = '#D3E7EE'
                elif 5 < y / (BRICK_HEIGHT + BRICK_SPACING) <= 7:
                    brick.color = '#ABD1DC'
                    brick.fill_color = '#ABD1DC'
                else:
                    brick.color = '#7097A8'
                    brick.fill_color = '#7097A8'

                self.window.add(brick, x=x, y=y + BRICK_OFFSET)

        # Score board
        self.lives_text = GLabel('default', x=0, y=20)
        self.lives_text.color = 'black'
        self.lives_text.font = '-20'
        self.window.add(self.lives_text)

        # Start button
        self.button_switch = True  # This variable is used to check whether the game starts
        self.start_button = GRect(PADDLE_WIDTH * 2, PADDLE_HEIGHT * 2)
        self.start_button.filled = True
        self.start_button.fill_color = 'black'
        self.start_button.color = 'black'
        self.start_text = GLabel('Click to start')
        self.start_text.color = 'white'
        self.start_text.font = '-20'
        self.window.add(self.start_button, x=(self.window_width - self.start_button.width) / 2, y=self.window_height - PADDLE_OFFSET * 4)
        self.window.add(self.start_text, x=(self.window_width - self.start_text.width) / 2, y=self.window_height - PADDLE_OFFSET * 4 + PADDLE_HEIGHT * 1.75)

    def game_start(self):
        # when the user click the mouse, it will trigger the event of button-disappear
        onmouseclicked(self.button_disappear)

    def button_disappear(self, click):
        # when the user clicks the button, the button will disappear and call breakout_game to start the game
        obj = self.window.get_object_at(click.x, click.y)
        if self.button_switch:
            if obj == self.start_button or obj == self.start_text:
                self.button_switch = False  # Close to prevent users to click
                self.window.remove(self.start_button)
                self.window.remove(self.start_text)
                self.breakout_game()

    def reset_game(self):
        # reset the ball's position to the original place
        self._ball.x = self.window_width / 2 - BALL_RADIUS
        self._ball.y = self.window_height / 2 - BALL_RADIUS

    def breakout_game(self):
        # When the user move the mouse, it will trigger the event of paddle-moving
        onmousemoved(self.paddle_moving)

    def paddle_moving(self, mouse):
        # When the user move the mouse, paddle will move left and right, but fix to a certain height
        self._paddle.x = mouse.x - self._paddle.width / 2
        self._paddle.y = self.window_height - PADDLE_OFFSET

    def is_ball_beyond_bottom(self):
        # This method is used to identify whether the ball reaches or goes beyond the bottom
        if self._ball.y > self.window.height - BALL_RADIUS:
            return True
        else:
            return False

    def ball_moving(self):
        # This method allows the ball to move by given (x,y) velocity
        self._ball.move(self._dx, self._dy)

    def bouncing_back(self):
        # When the ball collides to the top/right/left wall, the ball will bounce back
        if self._ball.x >= self.window_width - BALL_RADIUS or self._ball.x <= 0:  # right/left collision
            self._dx = - self._dx
        elif self._ball.y <= 0:  # top collision
            self._dy = -self._dy

    def collision(self):
        # Check if any corner of the ball has collided with the pall or bricks
        # If the ball collides with the paddle, the ball will bounce back
        # If the ball collides with any bricks, the ball will bounce back and the brick will disappear
        obj1 = self.window.get_object_at(self._ball.x, self._ball.y)
        obj2 = self.window.get_object_at(self._ball.x + 2 * BALL_RADIUS, self._ball.y)
        obj3 = self.window.get_object_at(self._ball.x, self._ball.y + 2 * BALL_RADIUS)
        obj4 = self.window.get_object_at(self._ball.x + 2 * BALL_RADIUS, self._ball.y + 2 * BALL_RADIUS)

        if obj1 is not None:
            if obj1 != self._paddle and obj1 != self.lives_text:
                self.window.remove(obj1)
                self._dy = - self._dy
            else:
                self._dy = - self._dy
        else:
            if obj2 is not None:
                if obj2 != self._paddle and obj2 != self.lives_text:
                    self.window.remove(obj2)
                    self._dy = - self._dy
                else:
                    self._dy = - self._dy
            else:
                if obj3 is not None:
                    if obj3 != self._paddle and obj3 != self.lives_text:
                        self.window.remove(obj3)
                        self._dy = - self._dy
                    else:
                        self._dy = - self._dy
                else:
                    if obj4 is not None:
                        if obj4 != self._paddle and obj4 != self.lives_text:
                            self.window.remove(obj4)
                            self._dy = - self._dy
                        else:
                            self._dy = - self._dy


def main():
    graphics = BreakoutGraphics()


if __name__ == '__main__':
    main()
