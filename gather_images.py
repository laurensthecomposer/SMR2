import cv2
import os
# import sys
import serial
import time

label_name = "none"
print( "Enter nr. of samples" )
num_samples = 110  # int(input())

IMG_SAVE_PATH = 'image_data'
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
    path = ''.join( [currentfolderpath, "/image_data/", label_name] )
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
        Arduino.write( b'f' )
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
        Arduino.write( b'f' )
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

            time.sleep(2)
            ret, frame = cap.read()
            ret, frame = cap.read()
            roi = frame[y_offset:y_offset + square_size, x_offset:x_offset + square_size]
            cv2.imshow( "roi", roi )
            cv2.imshow( "Collecting images", frame )
            k = cv2.waitKey( 100 )
            save_path = os.path.join( IMG_CLASS_PATH, '{}.jpg'.format( count + 1 ) )
            cv2.imwrite( save_path, roi )
            count += 1

            time.sleep( 1 )

            linetext = 0
            Arduino.write( b'f' )
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
