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

amount_train_images = 1296

amount_validation_images = 373

train_batch_size = 40

validation_batch_size = 20

train_it = datagen.flow_from_directory(os.path.abspath('image_data_better_camera_more_split/train'),target_size=(350,350), class_mode='categorical', batch_size=train_batch_size)

val_it = datagen.flow_from_directory(os.path.abspath('image_data_better_camera_more_split/validate'),target_size=(350,350), class_mode='categorical', batch_size=validation_batch_size)

amount_classes = len ( os.listdir(os.path.abspath('image_data_better_camera_more_split/train')) )




def get_model():
    model = Sequential([
        #change model res
        SqueezeNet(input_shape=(350, 350, 3), include_top=False),
        Dropout(0.5),
        Convolution2D(amount_classes, (1, 1), padding='valid'),
        Activation('relu'),
        GlobalAveragePooling2D(),
        Activation('softmax')
    ])
    return model

model = get_model()
model.compile(optimizer=Adam(lr=0.0001),loss='categorical_crossentropy', metrics=['acc'])

epochs = 4
model.fit_generator(train_it, steps_per_epoch=(amount_train_images/train_batch_size), validation_data=val_it, validation_steps=(amount_validation_images/validation_batch_size), epochs=epochs, verbose=1)

model_name = "swek""

name = os.path.join("ml_bolt_models", model_name)

# save the model for later use
model.save(name)

#score = model.evaluate(np.array(data), np.array(labels))

#print(score)
