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
import logger_csv

# Name of folder where to save data to
IMG_SAVE_PATH = 'image_test'
bolt_type_path = "nas6305-10"
num_samples = 100
rob_move = 0

# start Arduino connection
controller = arduino_controller.Arduino()

# Connect to robot & machine
# rob = sorting_robot.Robot()
machine = sorting_robot.SortingMachine()

# Calculate robot coordinates
# pickup_point, safe_pos, table_clear, pre_drop, zy_train, x_train = rob.get_waypoints()

# Set save path
count, num_samples, IMG_CLASS_PATH = machine.save_pictures( IMG_SAVE_PATH, bolt_type_path, num_samples )

# Setup camera
cap = machine.set_camera()

# Select data to be used in model
bolts = sorting_robot.Bolts()
REV_CLASS_MAP, model_name = bolts.bolts_in_model( sub_ass=1 )
model = load_model( model_name )

# Start machine
start = True

# setup pandas dataframe
column_names = ['foldername', 'filename', 'positive[T/F]', 'real_class', 'pred_class', 'pred_array']
logger = logger_csv.Logger(column_names, IMG_SAVE_PATH, 'test_log.csv' )
first_df_print = True


while True:
    if count == num_samples:
        controller.all_forward()
        time.sleep( 10 )
        controller.all_stop()
        break

    if start:
        controller.all_forward()

        if controller.gate_state:
            # print( 'found object, taking picture' )
            controller.all_stop()

            time.sleep( 4 )
            ret, frame = cap.read()
            ret, frame = cap.read()
            time.sleep( 2 )

            # show image
            cv2.imshow( "Collecting images", frame )
            k = cv2.waitKey( 100 )

            # save image
            filename = '{}.jpg'.format( count + 1 )
            save_path = os.path.join( IMG_CLASS_PATH, filename )
            cv2.imwrite( save_path, frame )

            # test image to model and output bolt type
            bolt_type, pred = machine.test_img( frame, model, REV_CLASS_MAP, size=(350, 350) )
            count += 1

            time.sleep( 1 )

            controller.all_forward()

            time.sleep( 0.5 )

            controller.all_stop()

            # Todo turn on for bolt drop
            # rob.drop(bolt_type, pickup_point, safe_pos, table_clear, pre_drop, zy_train, x_train, train=False)

            positive = (bolt_type_path == bolt_type)
            arr = [IMG_CLASS_PATH, filename, positive, bolt_type_path, bolt_type, pred]
            logger.append(arr)

            if first_df_print:
                logger.print_header()
                first_df_print = False
            logger.print_latest()

            # print( "Dropped: ", bolt_type )
            # print( "Accuracy: ", pred )

    k = cv2.waitKey( 1 )

    if k == ord( 'q' ):
        controller.all_stop()
        break

print( "\n{} image(s) saved in {}".format( count, IMG_CLASS_PATH ) )

cap.release()
cv2.destroyAllWindows()
