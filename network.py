import keras
from keras.applications import ResNet50
from keras.models import Model,Sequential
from keras.layers import Lambda, Dense, Dropout, Flatten, Conv2D, MaxPool2D, BatchNormalization
from keras.layers import GlobalAveragePooling2D, GaussianNoise, Input, Dropout, concatenate
from keras import optimizers
from keras.preprocessing.image import img_to_array
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import keras.backend as K
from keras.backend import tf as ktf

def model1(input_shape = (100,50,1), weights = None):
    model = ResNet50(weights='imagenet',include_top=False, input_shape=input_shape)
    inp = model.input
    x = model.output
    x = GlobalAveragePooling2D()(x)

    x = Dense(256, activation = 'relu')(x)
    out = Dense(1, name = 'reg', activation = 'sigmoid')(x)

    model = Model(inp, out)

    if weights:
        model.load_weights(weights)

    model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

    return model

def model2(input_shape = (100,50,1), weights = None):
    model = ResNet50(weights='imagenet',include_top=False, input_shape=input_shape)
    inp = model.input
    x = model.output
    x = GlobalAveragePooling2D()(x)

    x = Dense(256, activation = 'relu')(x)
    out = Dense(4, name = 'reg', activation = 'softmax')(x)

    model = Model(inp, out)

    if weights:
        model.load_weights(weights)

    model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
    return model
