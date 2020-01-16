from PIL import Image
import random
import os

debug_mode = True
output_file = "C:/Users/User/Desktop/img.jpeg"
width, height = 600, 600
size = (width, height)
img = Image.new('RGB', size)
pixels = img.load()
max = 80
colours = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for x in range(100)]

def inMandelbrotSet(c, m):
    z = 0
    for k in range(m):
        z = z**2 + c
        if abs(z) > 2:
            return (False, k)
    return (True, m)

for i in range(width):
    if debug_mode:
        if(i%(int(width/10)) == 0):
            print(str(int(i*100/width)) + "%")
    for j in range(height):
        inSet, iterations = inMandelbrotSet(complex(((i/width) * 2) - 1.5, ((j/height) * 2) - 1), max)
        if(inSet):
            pixels[i, j] = (0, 0, 0)
        else:
            pixels[i, j] = colours[int(iterations/max * len(colours))]

img.save(output_file, "JPEG")
os.system(output_file)
