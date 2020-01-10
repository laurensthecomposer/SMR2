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
from keras.callbacks import EarlyStopping

#TODO: tweak these values for stopping on the right time. See "Interesting Machine Learning/Existing machines" where to find info about this
earlystopping_callback = EarlyStopping(monitor = "val_loss", min_delta = 0, patience = 1, verbose = 1, mode = "auto")


datagen = ImageDataGenerator()

train_it = datagen.flow_from_directory('image_data_better_camera_more_split\\train',target_size=(227,227), class_mode='categorical', batch_size=89)

val_it = datagen.flow_from_directory('image_data_better_camera_more_split\\validate',target_size=(227,227), class_mode='categorical', batch_size=100)




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

# define the model
model = get_model()
model.compile(
    optimizer=Adam(lr=0.0001),
    loss='categorical_crossentropy',
    metrics=['acc']
)


# start training
epochs = 15
model.fit_generator(train_it, steps_per_epoch=10, callbacks=[earlystopping_callback], validation_data=val_it, validation_steps=1, epochs=epochs, verbose=1)


name = ''.join(["nas_class_set_v1.h5"])

# save the model for later use
model.save(name)

#score = model.evaluate(np.array(data), np.array(labels))

#print(score)
