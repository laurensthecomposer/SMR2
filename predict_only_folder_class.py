from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os

succes_rate = [0,0,0,0,0,0,0,0,0,0]
total_test = [0,0,0,0,0,0,0,0,0,0]
succes_percentage = [0,0,0,0,0,0,0,0,0,0]


folderpath = os.getcwd()
filepath = os.path.join(folderpath, "dataset/image_data_blue_light")
folder = 5  #change this for wich class you want to check
folder_path = os.path.join(filepath, "nas1802-3-8")  #change this for wich class you want to check

model = load_model("model/blue_light_split_tf1_sq550_e500_tb20_vb20_aug-hor-briran0_8;1_2.h5")

files = os.listdir(filepath)


REV_CLASS_MAP = {

   0: "m59557-10", # all correct
    1: "m59557-16", # all correct
    2: "m59557-20", # all correct
    3: "nas1802-3-6", # all correct
    4: "nas1802-3-7", # (1 incorrect with very LOW false-pos)
    5: "nas1802-3-8", # (2 incorrect MED and HIGH false-pos)
    6: "nas1802-3-9", # all correct
    7: "nas1802-4-07", # all correct
    8: "nas6305-10", # all correct
    9: "v647p23b" # all correct

}

def mapper(val):
    return REV_CLASS_MAP[val]


# print(boltname)
img_width, img_height = 550, 550

faulty = []
correct_amount = 0
boltname = files[folder]
picture_path = os.path.join(filepath, boltname)
picture_names = os.listdir(picture_path)
test_nr = 0
amount_test = len (picture_names) - 1
total_test[folder] = len (picture_names)


# load all images into a list
images = []
for img in os.listdir(folder_path):
    if img.startswith("."):
        continue
    img = os.path.join(folder_path, img)
    img = image.load_img(img, target_size=(img_width, img_height))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    images.append(img)

np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})
# stack up images list to pass for prediction
images = np.vstack(images)

i=0
classes = model.predict(images, batch_size=1)
for i in classes:

    pic_code = np.argmax(i)
    pic_name = mapper(pic_code)

    print("Predicted: {}".format(pic_name))
    # print(pic_code)
    print(i)
    if str(pic_name) == str(boltname):
            correct_amount += 1
            succes_rate[folder] = correct_amount
            # print(succes_rate)
            # print("Correct prediction")
    else:
        faulty.append(i)
    #test_nr += 1
succes_percentage[folder] = (succes_rate[folder] / total_test[folder]) * 100
print()
print(boltname, "   ", succes_percentage[folder], "% succesfull identification")

# print(total_test)
# print(succes_rate)
print(succes_percentage)
print("faulty ones are: ")
for i in faulty:
    print(i)