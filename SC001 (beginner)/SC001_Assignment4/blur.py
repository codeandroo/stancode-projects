"""
File: blur.py
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, allow users to input a SimpleImage object to this function
    :return: SimpleImage, return a SimpleImage object back
    """

    # Create a bigger blank image
    bigger_blank = SimpleImage.blank(img.width + 2, img.height + 2)

    # Create a final blank image
    actual_blank = SimpleImage.blank(img.width, img.height)

    # Assign pixels around the boundary with zero value
    for x in range(img.width + 2):
        for y in range(img.width + 2):
            if x == 0 or y == 0 or x == img.width + 1 or y == img.height + 1:
                bp = bigger_blank.get_pixel(x, y)
                bp.red = 0
                bp.green = 0
                bp.blue = 0

    # Copy the original image into the center of the bigger blank image
    for x in range(img.width):
        for y in range(img.height):
            p = img.get_pixel(x, y)
            bp = bigger_blank.get_pixel(x + 1, y + 1)

            bp.red = p.red
            bp.green = p.green
            bp.blue = p.blue

    # After the above 2 actions, every center pixel will all have 8 neighbor pixels
    for x in range(img.width):
        for y in range(img.height):
            count = 0

            p1 = bigger_blank.get_pixel(x, y)
            if x != 0 and y != 0:
                count += 1

            p2 = bigger_blank.get_pixel(x + 1, y)
            if x + 1 != 0 and y != 0:
                count += 1

            p3 = bigger_blank.get_pixel(x + 2, y)
            if x + 2 != 0 and y != 0:
                count += 1

            p4 = bigger_blank.get_pixel(x, y + 1)
            if x != 0 and y + 1 != 0:
                count += 1

            p5 = bigger_blank.get_pixel(x + 1, y + 1)
            if x + 1 != 0 and y + 1 != 0:
                count += 1

            p6 = bigger_blank.get_pixel(x + 2, y + 1)
            if x + 2 != 0 and y + 1 != 0:
                count += 1

            p7 = bigger_blank.get_pixel(x, y + 2)
            if x != 0 and y + 2 != 0:
                count += 1

            p8 = bigger_blank.get_pixel(x + 1, y + 2)
            if x + 1 != 0 and y + 2 != 0:
                count += 1

            p9 = bigger_blank.get_pixel(x + 2, y + 2)
            if x + 2 != 0 and y + 2 != 0:
                count += 1

            ap = actual_blank.get_pixel(x, y)

            ap.red = (p1.red + p2.red + p3.red + p4.red + p5.red + p6.red + p7.red + p8.red + p9.red) // count
            ap.green = (p1.green + p2.green + p3.green + p4.green + p5.green + p6.green + p7.green + p8.green + p9.green) // count
            ap.blue = (p1.blue + p2.blue + p3.blue + p4.blue + p5.blue + p6.blue + p7.blue + p8.blue + p9.blue) // count

    return actual_blank


def main():
    """
    This program will show an original picture and make the picture blurry.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
