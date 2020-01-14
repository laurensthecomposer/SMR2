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

datagen = ImageDataGenerator(featurewise_center=False,
                             samplewise_center=False,
                             featurewise_std_normalization=False,
                             samplewise_std_normalization=False,
                             zca_whitening=False,
                             zca_epsilon=1e-06,
                             rotation_range=0,
                             width_shift_range=0.0,
                             height_shift_range=0.0,
                             brightness_range=None,
                             shear_range=0.0,
                             zoom_range=0.0,
                             channel_shift_range=0.0,
                             fill_mode='nearest',
                             cval=0.0,
                             horizontal_flip=False,
                             vertical_flip=False,
                             rescale=None,
                             preprocessing_function=None,
                             data_format='channels_last',
                             validation_split=0.0,
                             interpolation_order=1,
                             dtype='float32')

def generate_data(train_batch_size, validation_batch_size):

    train_it = datagen.flow_from_directory(os.path.abspath('image_data_better_camera_more_split/train'),target_size=(350,350), class_mode='categorical', batch_size=train_batch_size)

    val_it = datagen.flow_from_directory(os.path.abspath('image_data_better_camera_more_split/validate'),target_size=(350,350), class_mode='categorical', batch_size=validation_batch_size)

    amount_classes = len ( os.listdir(os.path.abspath('image_data_better_camera_more_split/train')) )

    return train_it, val_it, amount_classes

def get_model(amount_classes):
    model = Sequential([
        #change model res
        SqueezeNet(input_shape=(350, 350, 3), include_top=False),
        Convolution2D(amount_classes, (1, 1), padding='valid'),
        Activation('relu'),
        GlobalAveragePooling2D(),
        Activation('softmax')
    ])
    return model


def make_model(train_it, val_it, amount_classes, train_batch_size, validation_batch_size, epochs=4):
    amount_train_images = 1296

    amount_validation_images = 373

    model = get_model(amount_classes)
    model.compile(optimizer=Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['acc'])  # lr = learning rate

    model.fit_generator(train_it, steps_per_epoch=(amount_train_images/train_batch_size), validation_data=val_it, validation_steps=(amount_validation_images/validation_batch_size), epochs=epochs, verbose=1)

    name = ''.join(["green_tes_v3_640px.h5"])

    # save the model for later use
    model.save(name)

#score = model.evaluate(np.array(data), np.array(labels))

#print(score)
if __name__ == "__main__":
    train_batch_size = 40
    validation_batch_size = 20
    train_it, val_it, amount_classes = generate_data(train_batch_size, validation_batch_size)
    make_model(train_it, val_it, amount_classes, train_batch_size, validation_batch_size)

