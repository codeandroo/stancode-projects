"""
File: stanCodoshop.py
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
1. Create a function to get the distance of pixel
2. Create a function to get the average number of a pixel's RGB
3. Create a function to get the best pixel by using #1 and #2
4. By using #3, rebuild the image to get a scenery picture without people around
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    color_dist = ((red - pixel.red) ** 2 + (green - pixel.green) ** 2 + (blue - pixel.blue) ** 2) ** (1 / 2)
    return color_dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    red_total = 0
    green_total = 0
    blue_total = 0
    for i in range(len(pixels)):
        red_total += pixels[i].red
        green_total += pixels[i].green
        blue_total += pixels[i].blue
    pixels_avg = [int(red_total / len(pixels)), int(green_total / len(pixels)), int(blue_total / len(pixels))]
    return pixels_avg


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    pixels_avg = get_average(pixels)
    shortest_dist = 0
    best_pixel = pixels[0]
    for i in range(len(pixels)):
        pixel_dist = get_pixel_dist(pixels[i], pixels_avg[0], pixels_avg[1], pixels_avg[2])
        if i == 0:  # The first distance is always the shortest one
            shortest_dist = pixel_dist
        elif pixel_dist < shortest_dist:  # Compare which distance is the shorter one
            shortest_dist = pixel_dist
            best_pixel = pixels[i]

    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect

    for x in range(width):
        for y in range(height):
            blank_pixel = result.get_pixel(x, y)
            pixel_lst = []  # Create an empty list to save pixels with the same position across different images

            for i in range(len(images)):
                pixel = images[i].get_pixel(x, y)
                pixel_lst.append(pixel)

            best_pixel = get_best_pixel(pixel_lst)  # Get the best pixel and assign it back to the blank image
            blank_pixel.red = best_pixel.red
            blank_pixel.green = best_pixel.green
            blank_pixel.blue = best_pixel.blue

    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
