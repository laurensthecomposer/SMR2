import tensorflow
print(tensorflow.__version__)
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
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
    8: "v647p23b"

}

def mapper(val):
    return REV_CLASS_MAP[val]
model_path = "/Users/marcdudley/Downloads/SMR2/models/image_data_blue_light_split_sq600_e160_tb60_vb60_aug-hor-rotran20-briran0_8;1_2).h5"
model_path = os.path.abspath(model_path)
model = load_model(model_path)

# image folder
folder_path = 'dataset/image_data_blue_light_split/test/m59557-10'
folder_path = os.path.abspath(folder_path)
# path to model

# dimensions of images
img_width, img_height = 600, 600



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

#classes2 = model.predict(images, batch_size=1)

np.set_printoptions(formatter={'float': lambda x: "{0:0.3f}".format(x)})

print(classes)




