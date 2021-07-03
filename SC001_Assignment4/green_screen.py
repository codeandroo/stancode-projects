"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: SimpleImage, allow users to input a SimpleImage object (background picture) to this function
    :param figure_img: SimpleImage, allow users to input a SimpleImage object (figure picture) to this function
    :return: SimpleImage, return a combined image (a SimpleImage object) back to users
    """
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            fp = figure_img.get_pixel(x, y)
            bp = background_img.get_pixel(x, y)
            bigger = max(fp.red, fp.blue)

            if fp.green > bigger * 2:
                fp.red = bp.red
                fp.green = bp.green
                fp.blue = bp.blue

    return figure_img


def main():
    """
    This program will combine two pictures into one.
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
