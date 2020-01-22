import tensorflow
print(tensorflow.__version__)
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import ImageDataGenerator
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

# model = load_model(os.path.abspath("models/image_data_blue_light_split_sq350_e120_tb40_vb40_aug-hor-rotran20-briran0_8;1_2.h5"))
model = load_model("/Users/marcdudley/Downloads/SMR2/models/image_data_blue_light_split_sq350_e120_tb40_vb40_aug-hor-rotran20-briran0_8;1_2.h5")
# model.summary()

# image folder
folder_path = 'dataset/image_data_blue_light_split/test/'
roi_square_size = 350
test_batch_size = 10

test_datagen = ImageDataGenerator()

test_it = test_datagen.flow_from_directory(
    os.path.abspath(folder_path ),
    target_size=(roi_square_size, roi_square_size),
    class_mode='categorical',
    batch_size=test_batch_size
)


# stack up images list to pass for prediction
# classes = model.predict(images, batch_size=1)
# loss, acc = model.evaluate(test_it, verbose=2)
prediction = model.predict(test_it, verbose=1)
type(prediction)
print(prediction)
# print(classes)
