#from generateData import generateDataByGameIds, getGameIdsBySummonerName
import tensorflow as tf
import numpy as np
import csv
import random
import time
import os

fileNames = []
for fileName in os.listdir("data"):
    fileNames.append(fileName)
#fileNames = ["tarzaned5", "sophist sage1", "pants are dragon", "santorin"]
wins = []
frames = []
data = []

for name in fileNames:
    file = open("data/{}".format(name), newline = "")
    reader = csv.reader(file,delimiter=",")
    for row in reader:
        data.append(row)
    file.close()
random.shuffle(data)

for d in data:
    wins.append(d[0])
    frames.append(d[2:]) #ignores who won and time
x_train,y_train = np.array(frames), np.array(wins)


#x_train = tf.keras.utils.normalize(x_train)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(1))
model.add(tf.keras.layers.Activation("sigmoid"))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=2)
model.save("model{}.model".format(time.time()))
