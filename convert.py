import sys
import numpy
from PIL import Image

def convert(image_file):
    #img_file = sys.argv[1]
    img = Image.open(image_file, 'r')
    width, height = 64, 64

    # Convert to PNG
    img = img.convert("RGBA")

    # Change image size
    img = img.resize((width, height))
    img.save("resize.png")
    width, height = img.size
    pixel_values = list(img.getdata())
    img_array = []
    for pixel in pixel_values:
        avg = (int(pixel[0]) + int(pixel[1]) + int(pixel[2]) + int(pixel[3]))/4
        if avg == 0:
            img_array.append(" ")
        elif avg > 0 and avg <= 25:
            img_array.append(".")
        elif avg > 25 and avg <= 50:
            img_array.append(":")
        elif avg > 50 and avg <= 75:
            img_array.append("-")
        elif avg > 75 and avg <= 100:
            img_array.append("=")
        elif avg > 100 and avg <= 125:
            img_array.append("+")
        elif avg > 125 and avg <= 150:
            img_array.append("*")
        elif avg > 150 and avg <= 175:
            img_array.append("#")
        elif avg > 175 and avg <= 200:
            img_array.append("%")
        else:
            img_array.append("@")

    count = 0
    for i in range(0,width*height):
        if(count < width-1):
            print(img_array[i], end=" ")
            count += 1
        else:
            print(img_array[i])
            count = 0
    print("\n")