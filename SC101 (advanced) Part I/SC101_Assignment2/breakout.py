"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()

    # Add animation loop here!
    lives = NUM_LIVES
    graphics.lives_text.text = f'You have: {lives} lives left.'

    while True:
        if lives > 0:
            graphics.game_start()
            if not graphics.button_switch:
                graphics.ball_moving()
                graphics.bouncing_back()
                graphics.collision()
                if graphics.is_ball_beyond_bottom():
                    lives -= 1
                    graphics.lives_text.text = f'You have: {lives} lives left.'
                    graphics.reset_game()
        else:
            break
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
