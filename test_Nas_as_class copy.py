from keras.models import load_model
import cv2.cv2 as cv2
import numpy as np
import sys




#filepath = "Users\laure\Documents\SMR2\augmenting_image\1.jpg"

filepath = "/Users/marcdudley/Downloads/SMR2/Untitled.jpg"


REV_CLASS_MAP = {

    0: "m59557-10",
    1: "m59557-16",
    2: "m59557-20",
    3: "nas1802-4-07",
    4: "nas1802_3_6-7-8-9",
    5: "nas6305-10",
    6: "none"
}

def mapper(val):
    return REV_CLASS_MAP[val]

model = load_model("with_NAS_as_a_classV2_7e_350pix.h5")

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
