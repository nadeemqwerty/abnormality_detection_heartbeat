import tensorflow as tf
import numpy as np
import cv2
import glob

numOfImagesPerInput = 100
size_x = 900
size_y = 1600

TYPE = {
	'normal': -1,
	'artifact': 0,
	'extrahls': 1,
	'murmur': 2,
	'extrasystol': 3
}

x_trn, y_trn = [], []

filename = glob.glob("/home/psg/data/set_a/*")

for fname in filename:
	name = fname.split('/')[-1].spit('.')[0]
	if(name.split('__')[0] == 'Aunlabelledtest'):
		continue
	for i in range(0,10):
		x_trn.append(cv2.imread(name + str(i) + '.jpeg'))
		normal = 0
		abnormalType = TYPE[name.split('__')[0]]
		if(name.split('__')[0] == 'normal'):
			normal = 1
		y_trn.append([normal,abnormalType])

x_trn = np.asarray(x_trn)
y_trn = np.asarray(y_trn)

np.save('x_trn', x_trn)
np.save('y_trn', y_trn)

inputs = tf.keras.layers.Input(shape=(numOfImagesPerInput, size_x, size_y, 3), name='inputs')

feature_map = tf.keras.layers.MaxPool3D(pool_size=(5, 5, 5), strides=2)(
    tf.keras.layers.Conv3D(32, (5, 5, 5), activation='relu')(
      tf.keras.layers.AvgPool3D(pool_size=(1, 5, 5), strides=2)(
        tf.keras.layers.Conv3D(64, (1, 3, 3), activation='relu')(
          inputs))))

output1 = tf.keras.layers.Dense(2, activation='sigmoid', name='output1')(tf.keras.layers.Dense(128, activation='relu')(tf.keras.layers.Dropout(0.2)(tf.keras.layers.Dense(256, activation='relu')(tf.keras.layers.Dense(256, activation='relu')(tf.keras.layers.Flatten()(feature_map))))))
output2 = tf.keras.layers.Dense(4, activation='sigmoid', name='output2')(tf.keras.layers.Dense(128, activation='relu')(tf.keras.layers.Dropout(0.2)(tf.keras.layers.Dense(256, activation='relu')(tf.keras.layers.Dense(256, activation='relu')(tf.keras.layers.Flatten()(feature_map))))))

model1 = tf.keras.Model(inputs=inputs, outputs=output1)

model2 = tf.keras.Model(inputs=inputs, outputs=output2)

model1.compile(optimizer='adam',
	loss='sparse_categorical_crossentropy',
	metrics=['accuracy'])

model2.compile(optimizer='adam',
	loss='sparse_categorical_crossentropy',
	metrics=['accuracy'])

