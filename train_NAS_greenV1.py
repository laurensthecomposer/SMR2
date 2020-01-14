from keras_squeezenet import SqueezeNet
from keras.optimizers import Adam
from keras.utils import np_utils
from keras.layers import Activation, Dropout, Convolution2D, GlobalAveragePooling2D
from keras.models import Sequential
import tensorflow as tf
import os
from keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator()

train_it = datagen.flow_from_directory('/Users/marcdudley/Downloads/SMR2/old_image_data/image_data_bc_nas_only/train',target_size=(750,750), class_mode='categorical', batch_size=40)

val_it = datagen.flow_from_directory('/Users/marcdudley/Downloads/SMR2/old_image_data/image_data_bc_nas_only/validate',target_size=(750,750), class_mode='categorical', batch_size=20)

def get_model():
    model = Sequential([
        #change model res
        SqueezeNet(input_shape=(750, 750, 3), include_top=False),
        Dropout(0.5),
        Convolution2D(4, (1, 1), padding='valid'),
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


model.fit_generator(train_it, steps_per_epoch=10, validation_data=val_it, validation_steps=1, epochs=epochs, verbose=1)


name = ''.join(["bc_NAS_only_v1_750pix.h5"])

# save the model for later use
model.save(name)

#score = model.evaluate(np.array(data), np.array(labels))

#print(score)