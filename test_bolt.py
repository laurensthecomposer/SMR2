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
IMG_SAVE_PATH = 'dataset/image_test'
bolt_type_path = "test_bolts"
num_samples = 100
rob_move = 0

# start Arduino connection
controller = arduino_controller.Arduino()

# Connect to robot & machine
rob = sorting_robot.Robot()
rob.startup(controller)
machine = sorting_robot.SortingMachine()



# Set save path
count, num_samples, IMG_CLASS_PATH = machine.save_pictures( IMG_SAVE_PATH, bolt_type_path, num_samples )

# Setup camera
cap = machine.set_camera()

# Select data to be used in model
bolts = sorting_robot.Bolts()
REV_CLASS_MAP, file_path = bolts.bolts_in_model( sub_ass=1 )
model = load_model( file_path )

# Start machine
start = True

np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

# setup pandas dataframe
column_names = ['foldername', 'filename', 'positive[T/F]', 'real_class', 'pred_class', 'pred_array']
logger = logger_csv.Logger(column_names, IMG_SAVE_PATH, 'test_log.csv' )
first_df_print = True
controller.bulk_feeder_start()
controller.blocker_close()

while True:
    # if count == num_samples:
    #     controller.blocker_open()
    #     controller.all_forward()
    #     controller.bulk_feeder_stop()
    #     time.sleep( 10 )
    #     controller.all_stop()
    #     break

    if start:
        controller.all_forward()

        if controller.gate_state:
            time.sleep(0.1) # prevents big bolt from bouncing
            # print( 'found object, taking picture' )
            controller.all_stop()
            controller.bulk_feeder_stop()
            time.sleep( 4 )
            ret, frame = cap.read()
            ret, frame = cap.read()

            # show image
            # cv2.imshow( "Collecting images", frame )
            # k = cv2.waitKey( 100 )

            # save image
            filename = '{}.jpg'.format( count + 1 )
            save_path = os.path.join( IMG_CLASS_PATH, filename )
            cv2.imwrite( save_path, frame )

            # test image to model and output bolt type
            # Todo put in right size of final images
            bolt_type, pred, bolt_code = machine.test_img(frame, model, REV_CLASS_MAP, size=(550, 550))



            count += 1

            controller.blocker_open()
            time.sleep(0.5)
            controller.all_forward()
            time.sleep( 0.4 )  # wait until object is gone (don't go lower)
            controller.blocker_close() #close gate

            time.sleep( 0.4 ) #bolt goes into robot/output

            controller.all_stop()

            # Todo turn on for bolt drop
            positive = (bolt_type_path == bolt_type)
            arr = [IMG_CLASS_PATH, filename, positive, bolt_type_path, bolt_type, pred]
            logger.append(arr)

            if first_df_print:
                logger.print_header()
                first_df_print = False
            logger.print_latest()
            print(pred)
            percentage = pred[bolt_code]
            if percentage < 1:
                bolt_type = "Disaproved"
            rob.drop(controller, bolt_type)
            controller.bulk_feeder_start()

            # print( "Dropped: ", bolt_type )
            # print( "Accuracy: ", pred )

    k = cv2.waitKey( 1 )

    if k == ord( 'q' ):
        controller.bulk_feeder_stop()
        controller.all_stop()
        break

print( "\n{} image(s) saved in {}".format( count, IMG_CLASS_PATH ) )

cap.release()
cv2.destroyAllWindows()
