        # Using the pillow library, we can read and write binary image files.




import sys

from PIL import Image   # PIL = Pillow Library - open, edit, resize, save images . Create gifs

images = [] #   store image objects

for arg in sys.argv[1:]:    #   [1:] - Take everything except the program name
    image = Image.open(arg)
    images.append(image)    #   Stores image inside list

images[0].save( #   Uses first image as the base GIF
"costumes.gif",
 save_all = True,
 append_images = [images[1]],
 duration = 200,
 loop = 0  # loop = 0 (infinity)
)


# to run this program - 
# python costumes.py costume1.gif costume2.gif
# code costumes.gif