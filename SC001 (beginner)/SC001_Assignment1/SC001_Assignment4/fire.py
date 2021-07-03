"""
File: fire.py
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: str, allow users to input a file path
    :return: SimpleImage, return an image (a SimpleImage object) back to users
    """
    img = SimpleImage(filename)
    for pixel in img:
        avg = (pixel.red + pixel.green + pixel.blue) // 3

        # When the red element is higher than avg * HURDLE_FACTOR, those pixels would be marked as red
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0

        # Others would be marked as grey
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg

    return img


def main():
    """
    This program will show a original photo and the one has been adjusted.
    The adjusted picture will indicate the range of a forest fire.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
