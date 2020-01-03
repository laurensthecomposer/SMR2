from keras.models import load_model
import cv2.cv2 as cv2
import numpy as np
import sys




#filepath = "Users\laure\Documents\SMR2\augmenting_image\1.jpg"

filepath = "/Users/marcdudley/Downloads/SMR2/image_data_split/nas1802-3-6 copy/26.jpg"


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
    9: "none"
}

def mapper(val):
    return REV_CLASS_MAP[val]

model = load_model("full_set_val_acc_97_v1.h5")

# prepare the image
img = cv2.imread(filepath)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.resize(img, (227, 227))

# predict the picture
pred = model.predict(np.array([img]))

# sets print of arrays to 2 decimal places
np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

pic_code = np.argmax(pred[0])
pic_name = mapper(pic_code)

print("Predicted: {}".format(pic_name))
print(pic_code)
print(pred)
