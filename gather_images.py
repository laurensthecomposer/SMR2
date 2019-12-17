import cv2
import os
# import sys
import serial
import time
import arduino_controller

# start Arduino connection
controller = arduino_controller.Arduino()

# Name of folder where to save data to
label_name = "nas1802-3-6"
#print( "Enter nr. of samples" )
num_samples = 100  # int(input())


# Name image save location & describe path
IMG_SAVE_PATH = 'image_data'
IMG_CLASS_PATH = os.path.join( IMG_SAVE_PATH, label_name )

# Check if image path exists
try:
    os.mkdir( IMG_CLASS_PATH )
    count = 0
except FileExistsError:
    # Find location of directory
    currentfolderpath = os.getcwd()
    path = ''.join( [currentfolderpath, "/image_data/", label_name] )
    available = os.listdir( str( path ) ) # Check the files in the directory

    if len( available ):  # if there are already files in the folder
        available = sorted( available, key=len ) # Sort files by name lenght
        lastfile = available[-1] # Select last file
        startnr = lastfile.replace( ".jpg", "" ) # Strip JPG from file name
        count = int( startnr ) # Start counting from selected number
        num_samples = count + num_samples
    else:
        count = 0

# Start video capture & camera settings
cap = cv2.VideoCapture( 1, cv2.CAP_DSHOW )
cap.set( cv2.CAP_PROP_FRAME_WIDTH, 1920 )
cap.set( cv2.CAP_PROP_FRAME_HEIGHT, 1080 )
cap.set( cv2.CAP_PROP_AUTOFOCUS, 0 )  # turn the autofocus off
cap.set( cv2.CAP_PROP_FOCUS, 5 )  # set the focus of camera
# print(cap.get(cv2.CAP_PROP_FOCUS))

start = False

print( "press a to start" )

square_size = 350
# x_offset = 820
x_offset = 700
y_offset = 375
start = True

while True:
    # ret, frame = cap.read()

    # if not ret:
    #     continue

    if count == num_samples:
        controller.all_forward()
        time.sleep( 10 )
        controller.all_stop()
        break

    # Set size for roi (region of interest)
    # cv2.rectangle( frame, (x_offset, y_offset), (x_offset + square_size, y_offset + square_size), (255, 255, 255), 2 )

    # After press of start loop for taking pictures after pressing start
    if start:

        if controller.gate_state:
            print( label_name, ",", count )

            controller.all_stop()
            time.sleep(3)

            # Flush buffer so 2 reads
            ret, frame = cap.read()
            ret, frame = cap.read()

            roi = frame[y_offset:y_offset + square_size, x_offset:x_offset + square_size]
            cv2.imshow( "roi", roi )
            cv2.imshow( "Collecting images", frame )

            k = cv2.waitKey( 100 )
            save_path = os.path.join( IMG_CLASS_PATH, '{}.jpg'.format( count + 1 ) )
            cv2.imwrite( save_path, roi )

            count += 1
            # time.sleep( 1 )

            controller.all_forward()
            time.sleep( 0.5 )  # wait until object is gone

            # # Backwards for quick data collection
            # controller.backwards()

    font = cv2.FONT_HERSHEY_SIMPLEX
    # cv2.putText( frame, "Collecting {}".format( count ),
    #              (5, 50), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA )
    # cv2.imshow( "Collecting images", frame )

    k = cv2.waitKey( 1 )
    # if k == ord( 'a' ): # Start
    #     controller.all_forward()
    #     start = not start

    controller.all_forward()

    if k == ord( 'q' ): # Exit program
        controller.all_stop()
        break

print( "\n{} image(s) saved in {}".format( count, IMG_CLASS_PATH ) )
cap.release()
cv2.destroyAllWindows()
