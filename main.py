import time

from PIL import Image
import os


formatTo = str
formatType = str

imagePaths = []
imagePath = str

# Get the user's home directory
home_dir = os.path.expanduser('~')

# Join the home directory and the Downloads directory
downloads_dir = os.path.join(home_dir, 'Downloads')


def main():

    print("Hello user!")
    print("If you would like to start out converting images, please press [ENTER]")
    input()
    getFormat()




def getFormat():
    global formatTo
    global formatType

    clearInterface()
    print("Please choose the format to convert your image.")
    print("Options:     ")
    print("        [1] PNG")
    print("        [2] JPG/JPEG")
    print("        [3] PDF")
    print("        [4] PSD")
    print("        [5] ICO")

    formatTo = input()

    if formatTo == "1":
        formatType = ".png"
        getContent()
    elif formatTo == "2":
        formatType = ".jpg"
        getContent()
    elif formatTo == "3":
        formatType = ".pdf"
        getContent()
    elif formatTo == "4":
        formatType = ".psd"
        getContent()
    elif formatTo == "5":
        formatType = ".ico"
        getContent()
    else:
        getFormat()

def getContent():
    global imagePaths
    global imagePath

    clearInterface()

    print("Convert to: " + formatType)
    print("Queue: " + len(imagePaths).__str__())
    print("")
    print("Please Drag & Drop your image file you want to convert.")
    print("After dropping press [ENTER] and go on till you are finished.")
    print("When finished -> leave line empty + press [ENTER]")
    print("")
    imagePath = input()

    if os.path.exists(imagePath):
        imagePaths.append(imagePath)
        getContent()
    else:
        optionsMenu()


def convertImages():

    if len(imagePaths) > 0:
        for imagepth in imagePaths:
            img = Image.open(imagepth)
            conimg = img.convert("RGB")
            filename = os.path.basename(imagepth)
            conimg.save(downloads_dir + f"\\{filename+formatType}")
            print(f"Converted: {filename+formatType} in {imagepth}")
        print("")
        print("Queue is finished :) Restart application to convert more.")
    else:
        print("No queue available. Try again in 3 sec")
        time.sleep(3)
        getContent()


def optionsMenu():

    global imagePath

    clearInterface()
    print(f"Given path does not exist: {imagePath}")
    print("")
    print("Options:")
    print("        [1]  Add another image")
    print("        [2]  Convert image queue")

    a = input()

    if a == "1":
        getContent()
    elif a == "2":
        convertImages()
    else:
        optionsMenu()


def clearInterface():
    for i in range(50):
        print("")


main()