# Third party modules
import numpy as np
import cv2
from PIL import Image
import os
from os import listdir
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
from rich import print
from rich.console import Console
from rich.table import Table

console = Console()
# To get the Image type RGB,L,RGBA,etc ...
def get_mode(image_path):
    image = Image.open(image_path,cv2.IMREAD_UNCHANGED)
    mode = image.mode
    return mode

def print_credits():
    table = Table(show_header=True)
    table.add_column("Author", style="yellow")
    table.add_column("Contact", style="yellow")
    table.add_row("Aman Kumar", "adeepraghuvanshi@gmail.com ")
    console.print(table)
    
def get_image(image_path):
    """Get a numpy array of an image so that one can access values[x][y]."""
    image = cv2.imread(image_path,cv2.IMREAD_UNCHANGED)
    pixel_values = np.array(image)
    return pixel_values
    # IF the change of modes of image is required then The image modes can be accessed using this snipet
    
    # mode = get_mode(image_path)
    # if image.mode == "RGB":
    #     channels = 3
    # elif image.mode == "L":
    #     channels = 1
    # elif image.mode == "RGBA":
    #     channels = 4
    # else:
    #     print("Unknown mode: %s" % image.mode)
    #     return None
    

# # get the path or directory


# To get the modes of different image file in the present directory
# for images in os.listdir(folder_dir):
#     if images == "cmp_image.py":
#         continue
#     result = get_mode(images)
#     print(result)

# To check all the files in the present directory
def main():
    a = input("Enter the Directory where you want to check the different Images Whether they are true or not!! in the form of D:\Photos\Snapseed")
    print()
    folder_dir = a
    for images1 in os.listdir(folder_dir):
        if (images1.endswith(".png") or images1.endswith(".jpg") or images1.endswith(".jpeg")):
            if images1 == "cmp_image.py":
                continue
            img1 = get_image(images1)
            print(img1[0])
            for images2 in os.listdir(folder_dir):
                if(images1 == images2):
                    continue
                if (images2.endswith(".png") or images2.endswith(".jpg") or images2.endswith(".jpeg")):
                # display
                    img2 = get_image(images2)
                    print(img2[0])

                    if np.array_equal(img1,img2):
                        print("Both the Images are same")
                        print("Image 1 :-",images1)
                        print("Image 2 :-",images2)
                    else:
                        print("Both the Images are different ...")
                        print("Image 1 :-",images1)
                        print("Image 2 :-",images2)

if __name__ == "__main__":                 
    cprint(figlet_format("Compare   IMAGES!!"), "green", attrs=["bold"])
    print_credits()
    print()
    main()