from PIL import Image
import os.path, sys

path = "/Users/marcdudley/Downloads/SMR2/green_tes/green_tes_train/ms9557-20"
dirs = os.listdir(path)

def crop():
    for item in dirs:
        fullpath = os.path.join(path,item)         #corrected
        if os.path.isfile(fullpath):
            im = Image.open(fullpath)
            f, e = os.path.splitext(fullpath)
            imCrop = im.crop((200, 200, 660, 660)) #corrected
            imCrop.save(f + 'Cropped.jpg', "JPEG", quality=100)

crop()