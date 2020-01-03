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



datagen = ImageDataGenerator()

train_it = datagen.flow_from_directory('/Users/marcdudley/Downloads/SMR2/old_image_data/archive3_train',target_size=(227,227), class_mode='categorical', batch_size=89)

val_it = datagen.flow_from_directory('/Users/marcdudley/Downloads/SMR2/old_image_data/archive3_val',target_size=(227,227), class_mode='categorical', batch_size=100)




IMG_SAVE_PATH = 'image_data'

CLASS_MAP = {

    "m59557-10": 0,
    "m59557-16": 1,
    "m59557-20": 2,
    "nas1802-3-6": 3,
    "nas1802-3-7": 4,
    "nas1802-3-8": 5,
    "nas1802-3-9": 6,
    "nas1802-4-07": 7,
    "nas6305-10": 8,
    "none": 9
}

NUM_CLASSES = len(CLASS_MAP)


def mapper(val):
    return CLASS_MAP[val]


def get_model():
    model = Sequential([
        #change model res
        SqueezeNet(input_shape=(227, 227, 3), include_top=False),
        Dropout(0.5),
        Convolution2D(NUM_CLASSES, (1, 1), padding='valid'),
        Activation('relu'),
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


data, labels = zip(*dataset)
labels = list(map(mapper, labels))



# one hot encode the labels
labels = np_utils.to_categorical(labels)

# define the model
model = get_model()
model.compile(
    optimizer=Adam(lr=0.0001),
    loss='categorical_crossentropy',
    metrics=['acc']
)


# start training

epochs = 15
model.fit_generator(train_it, steps_per_epoch=10, validation_data=val_it, validation_steps=1, epochs=epochs, verbose=1)


name = ''.join(["nas_class_set_v1.h5"])

# save the model for later use
model.save(name)

#score = model.evaluate(np.array(data), np.array(labels))

#print(score)
