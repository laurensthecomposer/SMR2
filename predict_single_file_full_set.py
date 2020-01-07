from keras.models import load_model
import cv2.cv2 as cv2
import numpy as np
import sys
import os



#filepath = "Users\laure\Documents\SMR2\augmenting_image\1.jpg"

filepath = "/Users/marcdudley/Downloads/SMR2/green_tes/green_tes_test/nas1802-3-9/21.jpg"
filepath = os.path.abspath(filepath)

REV_CLASS_MAP = {

    0: "m59557-16",
    1: "m59557-20",
    2: "nas1802-3-7",
    3: "nas1802-3-9",
    4: "nas6305-10",
    5: "v647p23b"
}

def mapper(val):
    return REV_CLASS_MAP[val]

model = load_model("/Users/marcdudley/Downloads/SMR2/green_tes_v2_350px.h5")

# prepare the image
img = cv2.imread(filepath)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (350, 350))

# predict the picture
pred = model.predict(np.array([img]))

# sets print of arrays to 2 decimal places
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

pic_code = np.argmax(pred[0])
pic_name = mapper(pic_code)

print("Predicted: {}".format(pic_name))
print(pic_code)
print(pred)
