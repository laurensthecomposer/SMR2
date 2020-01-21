import cv2
import os
# import sys
import serial
import time
import arduino_controller
import sorting_robot


# Name of folder where to save data to
IMG_SAVE_PATH = 'dataset/image_data_blue_light'

REV_CLASS_MAP = {
    0: "m59557-10",
    1: "m59557-16",
    2: "m59557-20",
    3: "nas1802-3-6",
    4: "nas1802-3-7",
    5: "nas1802-3-8",
    6: "nas1802-3-9",
    7: "nas1802-4-07",
    8: "nas6305-10",
    9: "v647p23b"
}
bolt_type = REV_CLASS_MAP[0]
num_samples = 50
count = 0
rob_move = 0

# amount before_move
# amount_test_bolts = 2

# start Arduino connection
controller = arduino_controller.Arduino()
controller.blocker_close()
# Connect to robot & machine
# rob = sorting_robot.Robot()
machine = sorting_robot.SortingMachine()

# Calculate robot coordinates
# pickup_point, safe_pos, table_clear, pre_drop, zy_train, x_train = rob.get_waypoints()

# Set save path
count, num_samples, IMG_CLASS_PATH = machine.save_pictures(IMG_SAVE_PATH, bolt_type, num_samples)

# Setup camera
cap = machine.set_camera()

# Start gather images on booth
start = True
print("Collecting test data started.")

while True:
    controller.all_forward()

    if count == num_samples:
        controller.blocker_open()
        controller.all_forward()
        time.sleep( 10 )
        controller.all_stop()
        break
    if start:
        if controller.gate_state:
            print(bolt_type, ",", count)
            time.sleep(0.1) #prevents big bolt from bouncing
            controller.all_stop()
            time.sleep(3)

            # Flush buffer so 2 reads
            ret, frame = cap.read()
            ret, frame = cap.read()

            cv2.imshow( "Collecting images", frame )
            cv2.waitKey(1)

            k = cv2.waitKey( 100 )
            save_path = os.path.join( IMG_CLASS_PATH, '{}.jpg'.format( count + 1 ) )
            cv2.imwrite( save_path, frame )

            count += 1
            rob_move += 1
            controller.blocker_open()
            time.sleep(0.5)
            controller.all_forward()
            
            time.sleep( 0.4 )  # wait until object is gone (don't go lower)
            controller.blocker_close() #close gate
            # if rob_move == amount_test_bolts:
            #     controller.all_stop()
            #     rob.drop(bolt_type, pickup_point, safe_pos, table_clear, pre_drop, zy_train, x_train, train=True)
            #     controller.all_forward()
                # rob_move = 0

    k = cv2.waitKey( 1 )

    if k == ord( 'q' ): # Exit program
        controller.all_stop()
        break

print( "\n{} image(s) saved in {}".format( count, IMG_CLASS_PATH ) )
cap.release()
cv2.destroyAllWindows()
