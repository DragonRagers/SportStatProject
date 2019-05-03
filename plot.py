import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from riotwatcher import RiotWatcher
from gameData import getGameFrames


gameid = 2988389854
#key = input("Enter Riot API key:")
key = "RGAPI-2eaeb8fc-7cdc-479b-8c98-1ed4abcc9189"
watcher = RiotWatcher(key)

data = getGameFrames(watcher, "na1", gameid)
time = [item[0] for item in data]

for i in range(len(data)):
    data[i] = data[i][1:]
data = np.array(data)

#data = np.array([[i] + [0]*19 for i in range(40)])

model = tf.keras.models.load_model("model.model")

predictions = model.predict(data)

t1 = [item[0] for item in predictions]
t2 = [1- item[0] for item in predictions]

plt.ylim(0, 1)
plt.xlabel("Time (minutes)")
plt.ylabel("Chance of Winning (%)")
plt.title("Chances of Winning vs Time")

plt.plot(time, [.5]*len(time), color = "black")
plt.plot(time, t1, color = "blue")
plt.plot(time, t2, color = "red")
plt.show()
