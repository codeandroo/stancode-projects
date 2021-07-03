"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, allow users to input a file path
    :return: SimpleImage, return an image (a SimpleImage object) back to users
    """
    img = SimpleImage(filename)
    blank_img = SimpleImage.blank(img.width, img.height * 2)

    for x in range(img.width):
        for y in range(img.height):
            p = img.get_pixel(x, y)
            bp_up = blank_img.get_pixel(x, y)
            bp_down = blank_img.get_pixel(x, img.height * 2 - 1 - y)

            bp_up.red = p.red
            bp_up.green = p.green
            bp_up.blue = p.blue

            bp_down.red = p.red
            bp_down.green = p.green
            bp_down.blue = p.blue

    return blank_img


def main():
    """
    This program allows user to mirror a photo vertically.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
