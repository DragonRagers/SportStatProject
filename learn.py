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
minuteData = []
data = []

#fileNames = ["tsm zven.csv"]
for name in fileNames:
    file = open("data/{}".format(name), newline = "")
    reader = csv.reader(file,delimiter=",")
    for row in reader:
        data.append(row)
    file.close()

for d in data:
    minute = int(d[1])
    while minute > len(minuteData) - 1:
        minuteData.append([])


    minuteData[minute].append((d[0], d[2:]))

for i,md in enumerate(minuteData):
    print(i, "minutes")
    wins = []
    frames = []
    for f in md:
        wins.append(f[0])
        frames.append(f[1])

    x_train,y_train = np.array(frames), np.array(wins)

    #x_train = tf.keras.utils.normalize(x_train)

    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
    model.add(tf.keras.layers.Dense(1))
    model.add(tf.keras.layers.Activation("sigmoid"))

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=5)
    model.save("nn/model{}.model".format(i))
