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

# datagen = ImageDataGenerator(featurewise_center=False,
#                              samplewise_center=False,
#                              featurewise_std_normalization=False,
#                              samplewise_std_normalization=False,
#                              zca_whitening=False,
#                              zca_epsilon=1e-06,
#                              rotation_range=0,
#                              width_shift_range=0.0,
#                              height_shift_range=0.0,
#                              brightness_range=None,
#                              shear_range=0.0,
#                              zoom_range=0.0,
#                              channel_shift_range=0.0,
#                              fill_mode='nearest',
#                              cval=0.0,
#                              horizontal_flip=False,
#                              vertical_flip=False,
#                              rescale=None,
#                              preprocessing_function=None,
#                              data_format='channels_last',
#                              validation_split=0.0,
#                              interpolation_order=1,
#                              dtype='float32')

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator()

# settings
train_batch_size = 20
val_batch_size = 20
roi_square_size = 350
epochs = 4
amount_train_images = 1296
amount_val_images = 373


train_it = train_datagen.flow_from_directory(
    os.path.abspath( 'image_data_better_camera_more_split/train' ),
    target_size=(roi_square_size, roi_square_size),
    class_mode='categorical',
    batch_size=train_batch_size
)

val_it = test_datagen.flow_from_directory(
    os.path.abspath( 'image_data_better_camera_more_split/validate' ),
    target_size=(roi_square_size, roi_square_size),
    class_mode='categorical',
    batch_size=val_batch_size
)

amount_classes = len( os.listdir( os.path.abspath( 'image_data_better_camera_more_split/train' ) ) )

def get_model(amount_classes):
    model = Sequential( [
        # change model res
        SqueezeNet( input_shape=(roi_square_size, roi_square_size, 3), include_top=False ),
        Convolution2D( amount_classes, (1, 1), padding='valid' ),
        Activation( 'relu' ),
        GlobalAveragePooling2D(),
        Activation( 'softmax' )
    ] )
    return model


# define the model
model = get_model( amount_classes )
model.compile(
    optimizer=Adam( lr=0.0001 ),
    loss='categorical_crossentropy',
    metrics=['acc']
)  # lr = learning rate

# start training
history = model.fit_generator( train_it, steps_per_epoch=2, validation_data=val_it,
                     validation_steps=2, epochs=epochs, verbose=1 )
# model.fit_generator(train_it, steps_per_epoch=10, validation_data=val_it, validation_steps=1, epochs=epochs,
# verbose=1)
name = 'green_tes_v3_640px.h5'

# save the model for later use
model.save( name )

# score = model.evaluate(np.array(data), np.array(labels))

# print(score)
