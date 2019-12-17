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

rob = sorting_robot.Robot()
pickup_point, safe_pos, table_clear, pre_drop, zy_train, x_train = rob.get_waypoints()


# REV_CLASS_MAP = {
#     0:"m59557-10",
#     1:"m59557-16",
#     2:"m59557-20",
#     3:"nas1802-3-6",
#     4:"nas1802-3-7",
#     5:"nas1802-3-8",
#     6:"nas1802-3-9",
#    7: "nas1802-4-07",
#     8:"nas6305-10",
#    9: "none"
# }

REV_CLASS_MAP = {
    0: "nas1802-3-6",
    1: "nas1802-3-7",
    2: "nas1802-3-8",
    3: "nas1802-3-9",
    4: "none"
}


def mapper(val):
    return REV_CLASS_MAP[val]

def mapper_nas18(val):
    return REV_CLASS_MAP2[val]


# model = load_model( "two_small_bolts_or_nothing.h5" )

model_name = "nas18.h5"

model = load_model(model_name)


def test_img(img):
    # prepare the image
    img = cv2.cvtColor( img, cv2.COLOR_BGR2RGB )
    img = cv2.resize( img, (227, 227) )
    cv2.imshow("test", img)

    # predict the picture
    pred = model.predict( np.array( [img] ) )

    # sets print of arrays to 2 decimal places
    np.set_printoptions( formatter={'float': lambda x: "{0:0.3f}".format( x )} )

    pic_code = np.argmax( pred[0] )
    pic_name = mapper( pic_code )
    print("Dropping: ", pic_name)
    return pic_name


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

cap = cv2cap = cv2.VideoCapture( 1, cv2.CAP_DSHOW )
cap.set( cv2.CAP_PROP_FRAME_WIDTH, 1920 )
cap.set( cv2.CAP_PROP_FRAME_HEIGHT, 1080 )
cap.set( cv2.CAP_PROP_AUTOFOCUS, 0 )  # turn the autofocus off
cap.set( cv2.CAP_PROP_FOCUS, 20 )  # set the focus of camera
cap.set(cv2.CAP_PROP_BRIGHTNESS, 128.0)
cap.set(cv2.CAP_PROP_CONTRAST, 128.0)
cap.set(cv2.CAP_PROP_SATURATION, 128.0)
cap.set(cv2.CAP_PROP_HUE, -1.0)  # 13.0
cap.set(cv2.CAP_PROP_GAIN, 4.0)
cap.set(cv2.CAP_PROP_EXPOSURE, -7.0)

# start Arduino connection

# start Arduino connection
controller = arduino_controller.Arduino()

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

    square_size = 650
    # x_offset = 820
    x_offset = 500
    y_offset = 120
    # cv2.rectangle( frame, (x_offset, y_offset), (x_offset + square_size, y_offset + square_size), (255, 255, 255), 2 )

    # arduino.readline()

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
            pic_name = test_img(roi)
            count += 1

            time.sleep( 1 )

            controller.all_forward()

            time.sleep( 0.5 )

            controller.all_stop()

            rob.drop(pic_name, pickup_point, safe_pos, table_clear, pre_drop, zy_train, x_train, train=False)
            print("Dropped: ", pic_name)

    font = cv2.FONT_HERSHEY_SIMPLEX
    # cv2.putText( frame, "Collecting {}".format( count ),
    #              (5, 50), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA )
    # cv2.imshow( "Collecting images", frame )

    k = cv2.waitKey( 10 )
    # if k == ord( 'a' ):
    #     start = not start

    if k == ord( 'q' ):
        controller.all_stop()
        break

print( "\n{} image(s) saved in {}".format( count, IMG_CLASS_PATH ) )
cap.release()
cv2.destroyAllWindows()
