from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os

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

# image folder
folder_path = '/Users/marcdudley/Downloads/SMR2/image_data/nas1802-3-6'
# path to model

# dimensions of images
img_width, img_height = 350, 350



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


