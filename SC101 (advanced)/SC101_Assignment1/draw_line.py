"""
File: draw_line.py
Name: Andrew Chao
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked
from campy.gui.events.timer import pause

SIZE = 20
DELAY = 500
window = GWindow(width=1000, height=1000, title='Line drawer')

click_count = 0

begin_x = 0
begin_y = 0

end_x = 0
end_y = 0

circle = GOval(SIZE, SIZE)


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    while True:
        onmouseclicked(circle_creation)
        # When the second click has been made, the line between 2 circles should be created
        if click_count > 0 and click_count % 2 == 0:
            line = GLine(x0=begin_x, y0=begin_y, x1=end_x, y1=end_y)
            window.add(line)
            window.remove(circle)

        # Create delay for program to run smoothly
        pause(DELAY)


def circle_creation(mouse):
    """
    This function is served as circle creation when every mouse click has been made.
    :param mouse: Object, allow users to track the motion of mouse
    :return: no return for this function
    """
    global click_count, begin_x, begin_y, end_x, end_y, circle

    click_count += 1

    # Save the position (x,y) of each circle, so that we can draw a line between them
    if click_count % 2 == 1:
        circle = GOval(SIZE, SIZE)
        window.add(circle, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)
        begin_x = mouse.x
        begin_y = mouse.y
    else:
        end_x = mouse.x
        end_y = mouse.y


if __name__ == "__main__":
    main()
