
from keras_squeezenet import SqueezeNet
from keras.optimizers import Adam
from keras.utils import np_utils
from keras.layers import Activation, Dropout, Convolution2D, GlobalAveragePooling2D
from keras.models import Sequential
import tensorflow as tf
import os
from keras.preprocessing.image import ImageDataGenerator


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


name = ''.join(["NAS_green_v1_350pix.h5"])

# save the model for later use
model.save(name)

#score = model.evaluate(np.array(data), np.array(labels))

#print(score)
