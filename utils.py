import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2
from scipy.io import wavfile

from scipy.io.wavfile import read

import librosa
import librosa.display

import os
import glob
from network import classifier_1d
dict1 = {'artifact':0,'extrahls':1,'extrastole':2, 'murmur':3,'normal':4,}


def unison_shuffled_copies(a, b):
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    return a[p], b[p]

def extract_features(audio_path):
    y, sr = librosa.load(audio_path)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    return mfccs

def resize(img, width = 200):

    d1 = img.shape[1]

    if img.shape[1]<width:
        delta_w = width - d1
        left, right = delta_w//2, delta_w-(delta_w//2)
        return cv2.copyMakeBorder(img, 0, 0, left, right, cv2.BORDER_CONSTANT, value=0)

    else :
        delta = int((d1 - width)/2)
        return img[:,delta:width+delta]

def transform_and_save_to_npy(folders_in,folder_out):

    inp = []
    labels = []
    for folder in folders_in:
        for filename in glob.iglob(folder):
            if os.path.exists(filename):
                label = os.path.basename(filename).split("_")[0]
                if librosa.get_duration(filename=filename)>=3:
                    if label not in ["Aunlabelledtest", "Bunlabelledtest"]:
                        inp.append(resize(extract_features(filename)))
                        labels.append(dict1[label])

    inp = np.array(inp)
    inp = inp.reshape((inp.shape[0],inp.shape[1],inp.shape[2],1))

    labels = np.array(labels)
    inp, labels = unison_shuffled_copies(inp,labels)

    np.save("data/"+"inp.npy",inp)
    np.save("data/"+"labels.npy",labels)

def transform_and_save_to_npy_1d(folders_in,folder_out):

    inp = []
    labels = []
    for folder in folders_in:
        for filename in glob.iglob(folder):
            if os.path.exists(filename):
                label = os.path.basename(filename).split("_")[0]

                if label not in ["Aunlabelledtest", "Bunlabelledtest"]:
                    rate,data = read(filename)
                    data = data.reshape(1,data.shape[0])
                    img = cv2.resize(data, (int((data.shape[1]/rate)*100),1) )
                    inp.append(resize(img, width=500))
                    labels.append(dict1[label])

    inp = np.array(inp)
#     inp = inp.reshape((inp.shape[0],inp.shape[1],inp.shape[2],1))

    labels = np.array(labels)
    inp, labels = unison_shuffled_copies(inp,labels)

    np.save("data/"+"inp_1d.npy",inp)
    np.save("data/"+"labels_1d.npy",labels)

def transform_and_save_to_npy_1d_part(folders_in,folder_out):

    inp = []
    labels = []
    for folder in folders_in:
        for filename in glob.iglob(folder):
            if os.path.exists(filename):
                label = os.path.basename(filename).split("_")[0]
                # print(filename)
                if label not in ["Aunlabelledtest", "Bunlabelledtest"]:
                    rate,data = read(filename)
                    # print(filename)

                    data = data.reshape(1,data.shape[0])
                    # print(data.shape)

                    for i in range(int(data.shape[-1]/rate)-1):
                        print(data.shape)
                        img = data[i*rate:(i+2)*rate]
                        img = cv2.resize(data, (500,1) )
                        inp.append(img)
                        labels.append(dict1[label])

    inp = np.array(inp)
#     inp = inp.reshape((inp.shape[0],inp.shape[1],inp.shape[2],1))

    labels = np.array(labels)
    inp, labels = unison_shuffled_copies(inp,labels)
    print(inp.shape)
    print(labels.shape)
    np.save("data/"+"inp_1d.npy",inp)
    np.save("data/"+"labels_1d.npy",labels)

def pred(filename):
    model = classifier_1d(weights = "weights/weight_1d.h5")
    rate,data = read(filename)
    data = data.reshape(1,data.shape[0])
    img = cv2.resize(data, (int((data.shape[1]/rate)*100),1))
    img = resize(img, width=500)
    img = img.reshape(1,img.shape[1], img.shape[0])

    out = model.predict(img)

    label = ['artifact','extrahls','extrastole', 'murmur','normal']

    i = np.argmax(out[0])
    return label[i],out[0][i]
