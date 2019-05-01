#from generateData import generateDataByGameIds, getGameIdsBySummonerName
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
import numpy as np
import csv

file = open("data.csv", newline = "")
reader = csv.reader(file,delimiter=",")

wins = []
frames = []
for row in reader:
    wins.append(row[0])
    frames.append(row[0:])

"""
 x_train, y_train = data
#x_train,y_train = makeData(False)
#x_train = tf.keras.utils.normalize(x_train, axis=1)
x_train = x_train / 255

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(16 activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(16, activation=tf.nn.relu))
#model.add(tf.keras.layers.Dense(32, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(13, activation=tf.nn.softmax))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=300)
model.save("model{}.model".format(time.time()))
"""
