import cv2
import os
# import sys
import serial
import time
from keras.models import load_model
import cv2.cv2 as cv2
import numpy as np
import sys

filepath = "C:/Users/laure/Documents/SMR2/image_data/bolt_m8x35/2.jpg"

REV_CLASS_MAP = {
    0: "bolt_m4x20",
    1: "bolt_m8x35",
    2: "none"
}


def mapper(val):
    return REV_CLASS_MAP[val]


model = load_model( "two_small_bolts_or_nothing.h5" )


def test_img(img):
    # prepare the image
    img = cv2.cvtColor( img, cv2.COLOR_BGR2RGB )
    img = cv2.resize( img, (227, 227) )

    # predict the picture
    pred = model.predict( np.array( [img] ) )

    # sets print of arrays to 2 decimal places
    np.set_printoptions( formatter={'float': lambda x: "{0:0.3f}".format( x )} )

    pic_code = np.argmax( pred[0] )
    pic_name = mapper( pic_code )

    print( "Predicted: {}".format( pic_name ) )
    print( pic_code )
    print( pred )


# ========
label_name = "test_bolts"
print( "Enter nr. of samples" )
num_samples = 110  # int(input())

IMG_SAVE_PATH = 'image_test'
IMG_CLASS_PATH = os.path.join( IMG_SAVE_PATH, label_name )

# print(IMG_CLASS_PATH)
try:
    os.mkdir( IMG_SAVE_PATH )
except FileExistsError:
    pass
try:
    os.mkdir( IMG_CLASS_PATH )
    count = 0
except FileExistsError:
    currentfolderpath = os.getcwd()
    path = ''.join( [currentfolderpath, "/image_test/", label_name] )
    available = os.listdir( str( path ) )
    if len( available ):  # if there are already files in the folder
        available = sorted( available, key=len )
        lastfile = available[-1]
        startnr = lastfile.replace( ".jpg", "" )
        count = int( startnr )
        # print("{} directory already exists.".format(IMG_CLASS_PATH))
        # print("All images gathered will be saved along with existing items in this folder")
        num_samples = count + num_samples
    else:
        count = 0

cap = cv2.VideoCapture( 1, cv2.CAP_DSHOW )
cap.set( cv2.CAP_PROP_FRAME_WIDTH, 1920 )
cap.set( cv2.CAP_PROP_FRAME_HEIGHT, 1080 )
cap.set( cv2.CAP_PROP_AUTOFOCUS, 0 )  # turn the autofocus off
cap.set( cv2.CAP_PROP_FOCUS, 5 )  # set the focus of camera
# print(cap.get(cv2.CAP_PROP_FOCUS))

start = False

# start Arduino connection

Arduino = serial.Serial( 'COM5', 9600, timeout=1 )
time.sleep( 2 )

print( "press a to start" )

while True:
    ret, frame = cap.read()

    if not ret:
        continue

    if count == num_samples:
        Arduino.write( b'r' )
        Arduino.flush()
        arduinoData = Arduino.readline().decode( 'ascii' )
        time.sleep( 10 )
        Arduino.write( b's' )
        Arduino.flush()
        arduinoData = Arduino.readline().decode( 'ascii' )

        break

    square_size = 350
    # x_offset = 820
    x_offset = 700
    y_offset = 365
    cv2.rectangle( frame, (x_offset, y_offset), (x_offset + square_size, y_offset + square_size), (255, 255, 255), 2 )

    # arduino.readline()

    if start:
        Arduino.write( b'r' )
        Arduino.flush()
        arduinoData = Arduino.readline().decode( 'ascii' )

        Arduino.write( b'l' )
        Arduino.flush()
        linetext = Arduino.readline().decode( "ascii" ).strip()

        if linetext == '1':
            print( 'found object, taking picture' )
            Arduino.write( b's' )
            Arduino.flush()
            arduinoData = Arduino.readline().decode( 'ascii' )

            time.sleep( 2 )
            ret, frame = cap.read()
            ret, frame = cap.read()
            roi = frame[y_offset:y_offset + square_size, x_offset:x_offset + square_size]
            cv2.imshow( "roi", roi )
            cv2.imshow( "Collecting images", frame )
            k = cv2.waitKey( 100 )
            save_path = os.path.join( IMG_CLASS_PATH, '{}.jpg'.format( count + 1 ) )
            cv2.imwrite( save_path, roi )
            test_img(roi)
            count += 1

            time.sleep( 1 )

            linetext = 0
            Arduino.write( b'r' )
            Arduino.flush()
            arduinoData = Arduino.readline().decode( 'ascii' )
            time.sleep( 4 )

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText( frame, "Collecting {}".format( count ),
                 (5, 50), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA )
    cv2.imshow( "Collecting images", frame )

    k = cv2.waitKey( 10 )
    if k == ord( 'a' ):
        start = not start

    if k == ord( 'q' ):
        break

print( "\n{} image(s) saved in {}".format( count, IMG_CLASS_PATH ) )
cap.release()
cv2.destroyAllWindows()
