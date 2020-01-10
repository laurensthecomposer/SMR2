from keras.models import load_model
import cv2.cv2 as cv2
import numpy as np
import sys
import os


# arrays for saving
succes_rate = [0,0,0,0,0,0,0,0,0,0]
succes_rate_global = [0,0,0,0,0,0,0,0,0,0]
total_test = [0,0,0,0,0,0,0,0,0,0]
succes_percentage = [0,0,0,0,0,0,0,0,0,0]
succes_percentage_global = [0,0,0,0,0,0,0,0,0,0]

#filepath = "Users\laure\Documents\SMR2\augmenting_image\1.jpg"


folderpath = os.getcwd()
main_folder = "image_data_better_camera_more_split"
filepath = os.path.join(folderpath, main_folder, "test")
threshold = 0.9

files = os.listdir(filepath)

amount = len (files) - 1

folder = 0

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
    9: "v647p23b",
    10: "wrong part"
}


def mapper(val):
    return REV_CLASS_MAP[val]

model = load_model("DennisModelTry1.h5")

while folder <= amount:
    correct_amount = 0
    correct_amount_global = 0
    boltname = files[folder]
    picture_path = os.path.join(filepath, boltname)
    picture_names = os.listdir(picture_path)
    test_nr = 0
    amount_test = len (picture_names) - 1
    total_test[folder] = len (picture_names)

    # print(boltname)
    while test_nr <= amount_test:
        picture_nr = picture_names[test_nr]
        picpath = os.path.join(picture_path, picture_nr)
        # prepare the image
        img = cv2.imread(picpath)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (350, 350))

        # predict the picture
        pred = model.predict(np.array([img]))

        # sets print of arrays to 2 decimal places
        np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

        pic_code = np.argmax(pred[0])
        pic_name = mapper(pic_code)

        print("Predicted: {}".format(pic_name))
        # print(pic_code)
        #print(pred)
        if np.max(pred[0]) <= threshold:
            pic_name_global = mapper(10)
        else:
            pic_name_global = pic_name
        if str(pic_name) == str(boltname):
            correct_amount += 1
            correct_amount_global += 1
            succes_rate[folder] = correct_amount
            succes_rate_global[folder] = correct_amount_global
            # print(succes_rate)
            # print("Correct prediction")
        elif str(pic_name_global) == "wrong part":
            correct_amount_global += 1
            succes_rate_global[folder] = correct_amount_global

        test_nr += 1
    succes_percentage[folder] = (succes_rate[folder] / total_test[folder]) * 100
    print(boltname, "   ", succes_percentage[folder], "% succesfull identification")
    succes_percentage_global[folder] = (succes_rate_global[folder] / total_test[folder]) * 100
    print(boltname, "   ", succes_percentage_global[folder], "% global succesfull identification")
    folder += 1


# print(total_test)
# print(succes_rate)
print(succes_percentage)
print(succes_percentage_global)

#
# filepath = 'C:/Users/marce/PycharmProjects/SMR2/green_tes/green_tes_test/v647p23b/31.jpg'
#
#
# REV_CLASS_MAP = {
#
#     0: "m59557-16",
#     1: "m59557-20",
#     2: "nas1802-3-7",
#     3: "nas1802-3-9",
#     4: "nas6305-10",
#     5: "v647p23b"
# }
#
# def mapper(val):
#     return REV_CLASS_MAP[val]
#
# model = load_model("C:/Users/marce/PycharmProjects/SMR2/green_tes_v1.h5")
#
# # prepare the image
# img = cv2.imread(filepath)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img = cv2.resize(img, (640, 640))
#
# # predict the picture
# pred = model.predict(np.array([img]))
#
# # sets print of arrays to 2 decimal places
# np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
#
# pic_code = np.argmax(pred[0])
# pic_name = mapper(pic_code)
#
# print("Predicted: {}".format(pic_name))
# print(pic_code)
# print(pred)
