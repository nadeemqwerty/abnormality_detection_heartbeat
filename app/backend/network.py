import keras
from keras.applications import ResNet50
from keras.models import Model,Sequential
from keras.layers import Lambda, Dense, Dropout, Flatten, Conv2D, MaxPool2D, BatchNormalization,GlobalMaxPool1D
from keras.layers import GlobalAveragePooling2D, GaussianNoise, Input, Dropout, concatenate,Convolution1D,MaxPool1D
from keras import optimizers
from keras.preprocessing.image import img_to_array
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import keras.backend as K
from keras.backend import tf as ktf


def classifier1(input_shape = (100,50,1), weights = None):
    model = ResNet50(weights='imagenet',include_top=False, input_shape=input_shape)
    inp = model.input
    x = model.output
    x = GlobalAveragePooling2D()(x)

    x = Dense(256, activation = '"relu"')(x)
    out = Dense(1, name = 'reg', activation = 'sigmoid')(x)

    model = Model(inp, out)

    if weights:
        model.load_weights(weights)

    model.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

    return model

def classifier2(input_shape = (100,50,1), weights = None):
    model = ResNet50(weights='imagenet',include_top=False, input_shape=input_shape)
    inp = model.input
    x = model.output
    x = GlobalAveragePooling2D()(x)

    x = Dense(256, activation = '"relu"')(x)
    out = Dense(4, name = 'reg', activation = 'softmax')(x)

    model = Model(inp, out)

    if weights:
        model.load_weights(weights)

    model.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
    return model

def classifier(input_shape = (40,200,1), weights = None):
    model = ResNet50(weights='imagenet',include_top=False, input_shape=input_shape)
    inp = model.input
    x = model.output
    x = GlobalAveragePooling2D()(x)

    x = Dense(256, activation = '"relu"')(x)
    out = Dense(5, name = 'classifier', activation = 'softmax')(x)

    model = Model(inp, out)

    # model = Sequential()
    # model.add(Conv2D(filters=16, kernel_size=2, input_shape=input_shape, activation='"relu"'))
    # model.add(MaxPool2D(pool_size=2))
    # model.add(Dropout(0.2))
    #
    # model.add(Conv2D(filters=32, kernel_size=2, activation='"relu"'))
    # model.add(MaxPool2D(pool_size=2))
    # model.add(Dropout(0.2))
    #
    # model.add(Conv2D(filters=64, kernel_size=2, activation='"relu"'))
    # model.add(MaxPool2D(pool_size=2))
    # model.add(Dropout(0.2))
    #
    # model.add(Conv2D(filters=128, kernel_size=2, activation='"relu"'))
    # model.add(MaxPool2D(pool_size=2))
    # model.add(Dropout(0.5))
    # model.add(GlobalAveragePooling2D())
    #
    # model.add(Dense(5, activation='softmax'))
# model.summary()
    if weights:
        model.load_weights(weights)

    model.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])
    return model


def classifier_1d(input_shape =(500,1) , weights = None):
    nclass = 5
    inp = Input(shape=input_shape)
    x = Convolution1D(16, kernel_size=5, activation="relu", padding="valid")(inp)
    x = Convolution1D(16, kernel_size=5, activation="relu", padding="valid")(x)
    x = MaxPool1D(pool_size=2)(x)
    x = Dropout(rate=0.1)(x)
    x = Convolution1D(32, kernel_size=3, activation="relu", padding="valid")(x)
    x = Convolution1D(32, kernel_size=3, activation="relu", padding="valid")(x)
    x = MaxPool1D(pool_size=2)(x)
    x = Dropout(rate=0.1)(x)
    x = Convolution1D(32, kernel_size=3, activation="relu", padding="valid")(x)
    x = Convolution1D(32, kernel_size=3, activation="relu", padding="valid")(x)
    x = MaxPool1D(pool_size=2)(x)
    x = Dropout(rate=0.1)(x)
    x = Convolution1D(256, kernel_size=3, activation="relu", padding="valid")(x)
    x = Convolution1D(256, kernel_size=3, activation="relu", padding="valid")(x)
    x = GlobalMaxPool1D()(x)
    x = Dropout(rate=0.2)(x)

    x = Dense(64, activation="relu", name="x")(x)
    x = Dense(64, activation="relu", name="dense_2")(x)
    x = Dense(nclass, activation="softmax", name="dense_3_mitbih")(x)

    model = Model(inp,x)

    if weights:
        model.load_weights(weights)

    opt = optimizers.Adam(0.001)

    model.compile(optimizer=opt, loss="sparse_categorical_crossentropy", metrics=['acc'])
    # model.summary()
    return model
