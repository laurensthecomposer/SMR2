from keras.models import load_model
from keras.preprocessing import image
import numpy as np
import os

REV_CLASS_MAP = {


# models/blue_light_crop_triple_sq550_e560_tb20_vb20_aug.h5, tested on 378 images 99.2pc correct

  #  0: "m59557-10", # all correct
   # 1: "m59557-16", # all correct
    #2: "m59557-20", # all correct
    #3: "nas1802-3-6", # all correct
    #4: "nas1802-3-7", # (1 incorrect with very LOW false-pos)
    #5: "nas1802-3-8", # (2 incorrect MED and HIGH false-pos)
    #6: "nas1802-3-9", # all correct
    #7: "nas1802-4-07", # all correct
    #8: "nas6305-10", # all correct
    #9: "v647p23b" # all correct



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

model = load_model("models/blue_light_split_tf1_sq550_e500_tb20_vb20_aug-hor-briran0_8;1_2.h5")

# image folder
folder_path = 'dataset/image_data_blue_light_more/nas1802-3-6'
# path to model

# dimensions of images
img_width, img_height = 550, 550


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

classes = model.predict_classes(images, batch_size=3)
print(classes)

