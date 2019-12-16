from keras.models import load_model
import cv2.cv2 as cv2
import numpy as np
import sys


filepath = "/Users/marcdudley/Downloads/SMR2/image_test/test_bolts/2.jpg"

REV_CLASS_MAP = {
    0: "bolt_m4x20",
    1: "bolt_m8x35",
    2: "none"
}

def mapper(val):
    return REV_CLASS_MAP[val]

model = load_model("two_small_bolts_or_nothing.h5")

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
