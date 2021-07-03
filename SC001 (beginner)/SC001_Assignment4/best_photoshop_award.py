"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""
from simpleimage import SimpleImage

THRESHOLD = 1.2
BLACK = 120


def main():
    """
    This program will combine two pictures into one.
    """
    andrew = SimpleImage("image_contest/andrew.png")
    thunder = SimpleImage("image_contest/thunder.jpeg")
    result = photoshop(andrew, thunder)
    result.show()


def photoshop(figure_pic, background_pic):

    background_pic.make_as_big_as(figure_pic)

    for x in range(figure_pic.width):
        for y in range(figure_pic.height):
            fp = figure_pic.get_pixel(x, y)
            avg = (fp.red + fp.blue + fp.green) // 3
            total = fp.red + fp.blue + fp.green
            bp = background_pic.get_pixel(x, y)

            if fp.green > avg * THRESHOLD and total > BLACK:
                fp.red = bp.red
                fp.blue = bp.blue
                fp.green = bp.green

    return figure_pic


if __name__ == '__main__':
    main()
