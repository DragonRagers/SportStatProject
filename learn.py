#from generateData import generateDataByGameIds, getGameIdsBySummonerName
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
import numpy as np
import csv
import random

file = open("data.csv", newline = "")
reader = csv.reader(file,delimiter=",")
next(reader) #skips the  coulum names


wins = []
frames = []
data = []
for row in reader:
    data.append(row)
random.shuffle(data)

for d in data:
    wins.append(d[0])
    frames.append(d[0:])
x_train,y_train = np.array(frames), np.array(wins)


#x_train = tf.keras.utils.normalize(x_train)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(64, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(64, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(2, activation=tf.nn.softmax))

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=50)
#model.save("model{}.model".format(time.time()))
