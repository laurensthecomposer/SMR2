import cv2.cv2 as cv2
import numpy as np
import os
import sys
import shutil
import crop_single_file
from sklearn.model_selection import train_test_split

IMG_SAVE_PATH = 'image_data_green'

NEW_SAVE_PATH = 'green_tes'

IMG_SAVE_PATH = os.path.abspath(IMG_SAVE_PATH)
NEW_SAVE_PATH = os.path.abspath(NEW_SAVE_PATH)

crop = {
    "pos_x": 520,
    "pos_y": 200,
    "width": 640,
    "height": 640
    ,
}

split_folders = {
    "train": 0.7,
    "validate": 0.2,
    "test": 0.1
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
            img_new = proccess_img( img, example=True )
            cv2.imshow( 'original', img )
            cv2.imshow( 'processed', img_new )
            print( 'example shown in cv2 window' )
            cv2.waitKey( 0 )
            cv2.destroyAllWindows()
            show_example_on_first = False
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # higher img res?
        # img = cv2.resize(img, (227, 227))

        proccess_img( img, new_path, item )

# load images from the directory
dataset = {}
# labels = list(map(mapper, labels))

# read all files and folders

for directory in os.listdir( NEW_SAVE_PATH ):
    path = os.path.join( NEW_SAVE_PATH, directory )
    if not os.path.isdir( path ):
        continue
    dataset[directory] = []
    for item in os.listdir( path ):
        # to make sure no hidden files get in our way
        if item.startswith( "." ):
            continue
        dataset[directory].append( item )

# create 3 folders

for split_folder in split_folders:
    create_dir( os.path.join( NEW_SAVE_PATH, split_folder ) )


def move_images(base_path, new_path, items):
    create_dir(new_path)
    for item in items:
        shutil.move( os.path.join( base_path, item ), os.path.join( new_path, item ) )


for category in dataset:
    y = dataset[category]

    y_train, y_test = train_test_split( y, test_size=split_folders['test'], random_state=1 )

    y_train, y_val = train_test_split( y_train, test_size=split_folders['validate'] / (1.0 - split_folders['test']),
                                       random_state=1 )

    # input basefolder, category, names

    base_path = os.path.join( NEW_SAVE_PATH, category )
    # train
    new_path = os.path.join( NEW_SAVE_PATH, 'train', category )
    move_images(base_path, new_path, y_train)

    # validate
    new_path = os.path.join( NEW_SAVE_PATH, 'validate', category )
    move_images(base_path, new_path, y_val)

    # test
    new_path = os.path.join( NEW_SAVE_PATH, 'test', category )
    move_images(base_path, new_path, y_test)

    shutil.rmtree( base_path )



