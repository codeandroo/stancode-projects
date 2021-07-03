"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

YOUR DESCRIPTION HERE
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x_coordinate = int((width / len(YEARS))) * year_index
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')  # delete all existing lines from the canvas

    # Write your code below this line
    #################################

    # Top fixed line
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE)

    # Bottom fixed line
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH - GRAPH_MARGIN_SIZE,
                       CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)

    # Reference lines and legends by years
    for i in range(len(YEARS)):
        canvas.create_line(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, i), 0,
                           GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, i), CANVAS_HEIGHT)
        canvas.create_text(GRAPH_MARGIN_SIZE + TEXT_DX + get_x_coordinate(CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, i),
                           CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                           text=YEARS[i], anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)  # draw the fixed background grid

    # Write your code below this line
    #################################
    name_order = 0  # This variable is used to store the order of the name in the list of lookup_names
    for name in lookup_names:
        x = []  # This list is used to store the x coordinates
        y = []  # This list is used to store the y coordinates
        rank = []  # This list is used to store the rank from each year
        year_str = []  # This list is used to store the string version of Years list
        color = COLORS[name_order % len(COLORS)]  # Color will take turn to be used based on the remainder of name_order

        # Covert the integer list of Year to the string list one
        for n in range(len(YEARS)):
            year_str.append(str(YEARS[n]))

        for i in range(len(YEARS)):
            x.append(GRAPH_MARGIN_SIZE + get_x_coordinate(CANVAS_WIDTH - 2 * GRAPH_MARGIN_SIZE, i))

        for yr in year_str:
            if yr in name_data[name]:
                y.append(int(name_data[name][yr]) * (CANVAS_HEIGHT - 2 * GRAPH_MARGIN_SIZE) / MAX_RANK + GRAPH_MARGIN_SIZE)
                rank.append(name_data[name][yr])
            else:
                y.append(CANVAS_HEIGHT - GRAPH_MARGIN_SIZE)
                rank.append('*')

        for j in range(len(x) - 1):
            canvas.create_line(x[j], y[j], x[j + 1], y[j + 1], fill=color, width=LINE_WIDTH)

        for k in range(len(x)):
            canvas.create_text(x[k] + TEXT_DX, y[k], text=name + ' ' + rank[k], anchor=tkinter.SW, fill=color)

        name_order += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
