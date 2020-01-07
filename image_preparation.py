import cv2.cv2 as cv2
import numpy as np
import os
import sys
import shutil
import crop_single_file

# load images from the directory
dataset = []

IMG_SAVE_PATH = 'image_data_green'

NEW_SAVE_PATH = 'image_augment_green'

CLASS_MAP = {

    "m59557-10": 0,
    "m59557-16": 1,
    "m59557-20": 2,
    "nas1802-3-6": 3,
    "nas1802-3-7": 4,
    "nas1802-3-8": 5,
    "nas1802-3-9": 6,
    "nas1802-4-07": 7,
    "nas6305-10": 8,
    "none": 9
}

NUM_CLASSES = len( CLASS_MAP )

crop = {
    "pos_x": 520,
    "pos_y": 200,
    "width": 640,
    "height": 640
    ,
}

split_folders = {
    "train": 70,
    "validate": 20,
    "test": 10
}

show_example_on_first = True


def create_dir(dirName):  # Create directory
    try:
        # Create target Directory
        os.mkdir( dirName )
        print( "Directory ", dirName, " Created " )
    except FileExistsError:
        print( "Directory ", dirName, " already exists" )


def empty_folder(folder_path):
    shutil.rmtree( folder_path )
    create_dir( folder_path )


create_dir( NEW_SAVE_PATH )


def proccess_img(img, new_path=None, item=None, example=False):
    img_crop = crop_single_file.crop( img, crop['pos_x'], crop['pos_y'], crop['width'], crop['height'] )
    if not example:
        cv2.imwrite( os.path.join( new_path, item ), img_crop )
    return img_crop


# check if items in folder

if os.listdir( NEW_SAVE_PATH ):
    answer = input( "Directory " + NEW_SAVE_PATH + " not empty. Do you want to empty (y/n): " )
    if answer == 'y':
        empty_folder( NEW_SAVE_PATH )
    else:
        print( "I will not make new files. Bye." )
        sys.exit()
else:
    print( NEW_SAVE_PATH + "is empty. Will automatically continue making new files in " + NEW_SAVE_PATH )

for directory in os.listdir( IMG_SAVE_PATH ):
    path = os.path.join( IMG_SAVE_PATH, directory )
    new_path = os.path.join( NEW_SAVE_PATH, directory )
    create_dir( new_path )
    if not os.path.isdir( path ):
        continue
    print( path )
    for item in os.listdir( path ):
        # to make sure no hidden files get in our way
        if item.startswith( "." ):
            continue
        img = cv2.imread( os.path.join( path, item ) )
        if show_example_on_first:
            img_new = proccess_img( img, example = True )
            cv2.imshow( 'original', img )
            cv2.imshow( 'processed', img_new )
            cv2.waitKey( 0 )
            cv2.destroyAllWindows()
            show_example_on_first = False
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # higher img res?
        # img = cv2.resize(img, (227, 227))
        # dataset.append( [path, directory] )
        proccess_img(img, new_path, item)

