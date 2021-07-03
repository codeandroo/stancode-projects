"""
File: shrink.py
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, allow users to input a file path
    :return img: SimpleImage, return an image (a SimpleImage object) back to users
    """
    img = SimpleImage(filename)
    blank_img = SimpleImage.blank(img.width // 2, img.height // 2)

    for x in range(0, img.width):
        for y in range(0, img.height):
            if x % 2 == 0 and y % 2 == 0:
                p1 = img.get_pixel(x, y)
                p2 = img.get_pixel(x + 1, y)
                p3 = img.get_pixel(x, y + 1)
                p4 = img.get_pixel(x + 1, y + 1)

                bp = blank_img.get_pixel(x/2, y/2)

                bp.red = (p1.red + p2.red + p3.red + p4.red) // 4
                bp.green = (p1.green + p2.green + p3.green + p4.green) // 4
                bp.blue = (p1.blue + p2.blue + p3.blue + p4.blue) // 4

    return blank_img


def main():
    """
    This program will show an original picture and make the picture 1/2 smaller.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()