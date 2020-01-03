import cv2.cv2 as cv2
import numpy as np
from keras_squeezenet import SqueezeNet
from keras.optimizers import Adam
from keras.utils import np_utils
from keras.layers import Activation, Dropout, Convolution2D, GlobalAveragePooling2D
from keras.models import Sequential
import tensorflow as tf
import os
from keras.preprocessing.image import ImageDataGenerator




IMG_SAVE_PATH = '/Users/marcdudley/Downloads/SMR2/image_data_b/bolts_none_b'

IMG_SAVE_PATH_VAL = '/Users/marcdudley/Downloads/SMR2/image_data_b/bolts_none_VAL_b'

datagen = ImageDataGenerator()

val_it = datagen.flow_from_directory('/Users/marcdudley/Downloads/SMR2/image_data_b/bolts_none_VAL_b', class_mode='categorical', batch_size=24)

train_it = datagen.flow_from_directory('/Users/marcdudley/Downloads/SMR2/image_data_b/bolts_none_b', class_mode='categorical', batch_size=91)

CLASS_MAP = {


    "nas1802-3-6_b": 0,
    "nas1802-3-7_b": 1,
    "nas1802-3-8_b": 2,
    "nas1802-3-9_b": 3,
    "none_b": 4
}

NUM_CLASSES = len(CLASS_MAP)


def mapper(val):
    return CLASS_MAP[val]


def get_model():
    model = Sequential([
        #change model res
        SqueezeNet(input_shape=(256, 256, 3), include_top=False),
        Dropout(0.5),
        Convolution2D(NUM_CLASSES, (1, 1), padding='same'),
        Activation('selu'),
        GlobalAveragePooling2D(),
        Activation('softmax')
    ])
    return model


# load images from the directory
dataset = []
for directory in os.listdir(IMG_SAVE_PATH):
    path = os.path.join(IMG_SAVE_PATH, directory)
    if not os.path.isdir(path):
        continue
    for item in os.listdir(path):
        # to make sure no hidden files get in our way
        if item.startswith("."):
            continue
        img = cv2.imread(os.path.join(path, item))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #higher img res?
        img = cv2.resize(img, (227, 227))
        dataset.append([img, directory])


dataset_VAL = []
for directory in os.listdir(IMG_SAVE_PATH_VAL):
    path_VAL = os.path.join(IMG_SAVE_PATH_VAL, directory)
    if not os.path.isdir(path_VAL):
        continue
    for item in os.listdir(path_VAL):
        # to make sure no hidden files get in our way
        if item.startswith("."):
            continue
        img = cv2.imread(os.path.join(path_VAL, item))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #higher img res?
        img = cv2.resize(img, (227, 227))
        dataset_VAL.append([img, directory])

data, labels = zip(*dataset)

#data_VAL = zip(*dataset_VAL)

labels = list(map(mapper, labels))




# one hot encode the labels
labels = np_utils.to_categorical(labels)


# define the model
model = get_model()
model.compile(
    optimizer=Adam(lr=0.001),
    loss='categorical_crossentropy',
    metrics=['acc']
)



# start training

epochs = 2
#model.fit(np.array(data), np.array(labels), validation_data=(val_it, np.array(labels)),  epochs=epochs, batch_size=10, verbose=2)
#validation_data=(np.array(data_VAL), np.array(labels)),

model.fit_generator(train_it, steps_per_epoch=2, validation_data=val_it, validation_steps=2, epochs=epochs, verbose=1)

name = ''.join(["nas_class_set_v1.h5"])

# save the model for later use
model.save(name)

#score = model.evaluate(np.array(data), np.array(labels))


