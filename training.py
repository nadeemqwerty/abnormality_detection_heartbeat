import numpy as np
from network import classifier, classifier_1d
from utils import resize
from scipy.io.wavfile import read


def train(epochs=16, batch_size=32):
    model = classifier()

    data_dir = "data/"

    inp = np.load(data_dir+"inp.npy")
    labels = np.load(data_dir+"labels.npy")
    print(inp.shape)
    print(labels.shape)

    model.summary()

    history = model.fit(inp, labels, epochs=epochs, batch_size=batch_size, shuffle=True,validation_split = 0.2,verbose=1)
    model.save_weights("weights/weight.h5")

# train(epochs = 32, batch_size = 32)

def train_1d(epochs=16, batch_size=32):
    model = classifier_1d()

    data_dir = "data/"

    inp = np.load(data_dir+"inp_1d.npy")
    inp = inp.reshape(inp.shape[0],500,1)
    labels = np.load(data_dir+"labels_1d.npy")
    print(inp.shape)
    print(labels.shape)

    model.summary()

    history = model.fit(inp, labels, epochs=epochs, batch_size=batch_size, shuffle=True,validation_split = 0.2,verbose=1)
    model.save_weights("weights/weight_1d.h5")

# def pred_1d(filename):
#     model = classifier_1d(weights = "weights/weight_1d.h5")
#     rate,data = read(filename)
#     data = data.reshape(1,data.shape[0])
#     img = cv2.resize(data, (int((data.shape[1]/rate)*100),1))
#     img = resize(img, width=500)
#     img = img.reshape(1,img.shape[1], img.shape[0])
#
# data_dir = "data/"
# # train_1d(epochs = 48, batch_size = 32)
# model = classifier_1d(weights = "weights/weight_1d.h5")
# inp = np.load(data_dir+"inp_1d.npy")
# inp = inp.reshape(inp.shape[0],500,1)
# labels = np.load(data_dir+"labels_1d.npy")
# eval = model.evaluate(inp,labels)
# print(eval)
