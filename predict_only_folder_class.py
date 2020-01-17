from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os

REV_CLASS_MAP = {


    0: "nas1802-3-6",
    1: "nas1802-3-7",



   # 0: "m59557-16",
    #1: "m59557-20",
    #2: "nas1802-3-7",
    #3: "nas1802-3-9",
    #4: "nas6305-10",
    #5: "v647p23b",

}

def mapper(val):
    return REV_CLASS_MAP[val]

model = load_model("/Users/marcdudley/Downloads/SMR2/green_tes_v2_350px.h5")

# image folder
folder_path = '/Users/marcdudley/Downloads/SMR2/green_tes/test/nas1802-3-7'
# path to model

# dimensions of images
img_width, img_height = 350, 350


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

# stack up images list to pass for prediction
images = np.vstack(images)
classes = model.predict(images, batch_size=1)
print(classes)