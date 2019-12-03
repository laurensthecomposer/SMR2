desc = '''Script to gather data images with a particular label.

Usage: python gather_images.py <label_name> <num_samples>

The script will collect <num_samples> number of images and store them
in its own directory.

Only the portion of the image within the box displayed
will be captured and stored.

Press 'a' to start/pause the image collecting process.
Press 'q' to quit.

'''

import cv2
import os
import sys
import serial
import time


label_name = "test"
print("Enter nr. of samples")
num_samples = int(input())


IMG_SAVE_PATH = 'image_data'
IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, label_name)

try:
    os.mkdir(IMG_SAVE_PATH)
except FileExistsError:
    pass
try:
    os.mkdir(IMG_CLASS_PATH)
    count = 0
except FileExistsError:
    currentfolderpath = os.getcwd()
    path = ''.join([currentfolderpath,"/image_data/", label_name])
    available = os.listdir(str(path))
    available = sorted(available, key=len)
    lastfile = available[-1]
    startnr = lastfile.replace(".jpg","")
    count = int(startnr)
    print("{} directory already exists.".format(IMG_CLASS_PATH))
    print("All images gathered will be saved along with existing items in this folder")
    num_samples = count + num_samples

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_AUTOFOCUS, 0)

start = False

# start Arduino connection

# arduino = serial.Serial('COM5', 115200)
time.sleep(1)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    if count == num_samples:
        # start for looping with picture by picture
        # print("Do you want to take more samples")
        # a = input()
        # if a == "Y":
        #     print("Give new amount of samples")
        #     num_samples = num_samples + int(input())
        # else:
            break

    cv2.rectangle(frame, (100, 100), (500, 500), (255, 255, 255), 2)


    # arduino.readline()

    if start:
        roi = frame[100:500, 100:500]
        save_path = os.path.join(IMG_CLASS_PATH, '{}.jpg'.format(count + 1))
        cv2.imwrite(save_path, roi)
        count += 1

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Collecting {}".format(count),
            (5, 50), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow("Collecting images", frame)

    k = cv2.waitKey(10)
    if k == ord('a'):
        start = not start

    if k == ord('q'):
        break

print("\n{} image(s) saved in {}".format(count, IMG_CLASS_PATH))
cap.release()
cv2.destroyAllWindows()
