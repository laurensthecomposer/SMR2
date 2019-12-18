import cv2
import os
# import sys
import arduino_controller
import time
from keras.models import load_model
import cv2.cv2 as cv2
import numpy as np
import sys
import sorting_robot

# Name of folder where to save data to
IMG_SAVE_PATH = 'image_test'
bolt_type = "test_bolts"
num_samples = 100
rob_move = 0

# start Arduino connection
controller = arduino_controller.Arduino()

# Connect to robot & machine
rob = sorting_robot.Robot()
machine = sorting_robot.SortingMachine()

# Calculate robot coordinates
pickup_point, safe_pos, table_clear, pre_drop, zy_train, x_train = rob.get_waypoints()

# Set save path
count, num_samples, IMG_CLASS_PATH = machine.save_pictures(IMG_SAVE_PATH, bolt_type, num_samples)

# Setup camera
cap = machine.set_camera()

# Size of region of interest
square_size = 650
x_offset = 200
y_offset = 120

# Select data to be used in model
bolts = sorting_robot.Bolts()
REV_CLASS_MAP, model_name = bolts.bolts_in_model(sub_ass=2)
model = load_model(model_name)

# Start machine
start = True


while True:
    if count == num_samples:
        controller.all_forward()
        time.sleep( 10 )
        controller.all_stop()
        break

    if start:
        controller.all_forward()

        if controller.gate_state:
            print( 'found object, taking picture' )
            controller.all_stop()

            time.sleep( 2 )
            ret, frame = cap.read()
            ret, frame = cap.read()

            roi = frame[y_offset:y_offset + square_size, x_offset:x_offset + square_size]
            img1 = cv2.cvtColor(roi, cv2.COLOR_RGB2GRAY)

            height, width = img1.shape

            h_centre = int(height / 2)
            w_centre = int(width / 2)

            thickness = 100

            cv2.circle(roi, (h_centre, w_centre), w_centre + int(thickness / 2), (0, 0, 0), thickness=thickness)

            cv2.imshow( "roi", roi )
            cv2.imshow( "Collecting images", frame )
            k = cv2.waitKey( 100 )
            save_path = os.path.join( IMG_CLASS_PATH, '{}.jpg'.format( count + 1 ) )
            cv2.imwrite( save_path, roi )
            # Test image to model and output bolt type
            bolt_type = machine.test_img(roi, model, REV_CLASS_MAP, size=(227, 227))
            count += 1

            time.sleep( 1 )

            controller.all_forward()

            time.sleep( 0.5 )

            controller.all_stop()

            # Todo turn on for bolt drop
            # rob.drop(bolt_type, pickup_point, safe_pos, table_clear, pre_drop, zy_train, x_train, train=False)
            print("Dropped: ", bolt_type)


    k = cv2.waitKey( 1 )

    if k == ord( 'q' ):
        controller.all_stop()
        break

print( "\n{} image(s) saved in {}".format( count, IMG_CLASS_PATH ) )
cap.release()
cv2.destroyAllWindows()
