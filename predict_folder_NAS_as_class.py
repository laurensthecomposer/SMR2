from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os

REV_CLASS_MAP = {


    0: "nas1802-3-6",
    1: "nas1802-3-7",
    2: "nas1802-3-8",
    3: "nas1802-3-9",

}

def mapper(val):
    return REV_CLASS_MAP[val]

model = load_model("/Users/marcdudley/Downloads/SMR2/bc_NAS_only_v1_750pix.h5")

# image folder
folder_path = '/Users/marcdudley/Downloads/SMR2/old_image_data/image_data_bc_nas_only/test/nas1802-3-6'
# path to model

# dimensions of images
img_width, img_height = 550, 550



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
classes = model.predict(images, batch_size=1)

classes2 = model.predict_classes(images, batch_size=1)

np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

print(classes)

print(classes2)


