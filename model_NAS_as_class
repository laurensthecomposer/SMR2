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

# separated validation and training data using image data generator and showing results
# attempted img augmentation, decided it wasn't stable enough
# built model with all types
# built model with NAS-03-06 to 09 bolts as a class
# created testing of whole folders


#recommendsations from experimenting:

# need more consistant pictures, including angle, noiseless background, lighting conditions
# pics at source of img size, 350 px works well for model using NAS-03-06 as a class
# need extra pics for testing not just validation and training pics
# retest images that fall below a certain threshold such as 70%
# make a class (status class) from standing bolts

datagen = ImageDataGenerator()

train_it = datagen.flow_from_directory('/Users/marcdudley/Downloads/SMR2/data_full_set_wo_nas/set_train',target_size=(350,350), class_mode='categorical', batch_size=74)

val_it = datagen.flow_from_directory('/Users/marcdudley/Downloads/SMR2/data_full_set_wo_nas/set_val',target_size=(350,350), class_mode='categorical', batch_size=75)



def get_model():
    model = Sequential([
        #change model res
        SqueezeNet(input_shape=(350, 350, 3), include_top=False),
        Dropout(0.5),
        Convolution2D(7, (1, 1), padding='valid'),
        Activation('relu'),
        GlobalAveragePooling2D(),
        Activation('softmax')
    ])
    return model






# define the model
model = get_model()
model.compile(
    optimizer=Adam(lr=0.0001),
    loss='categorical_crossentropy',
    metrics=['acc']
)


# start training

epochs = 7
model.fit_generator(train_it, steps_per_epoch=8, validation_data=val_it, validation_steps=1, epochs=epochs, verbose=1)


name = ''.join(["with_NAS_as_a_classV2_7e_350pix.h5"])

# save the model for later use
model.save(name)

#score = model.evaluate(np.array(data), np.array(labels))

#print(score)
