from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os

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

model = load_model("/Users/marcdudley/Downloads/SMR2/full_set_val_acc_97_v1.h5")

# image folder
folder_path = '/Users/marcdudley/Downloads/SMR2/old_image_data/archive3_val/nas1802-3-7'
# path to model

# dimensions of images
img_width, img_height = 227, 227



# load all images into a list
images = []
for img in os.listdir(folder_path):
    img = os.path.join(folder_path, img)
    img = image.load_img(img, target_size=(img_width, img_height))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    images.append(img)

# stack up images list to pass for prediction
images = np.vstack(images)
classes = model.predict_classes(images, batch_size=1)
print(classes)