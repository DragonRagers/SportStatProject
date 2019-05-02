import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from riotwatcher import RiotWatcher
from gameData import getGameFrames

gameid = 3019589039
watcher = RiotWatcher("RGAPI-bf4639fd-d553-4309-bbae-b87b43900c42")
data = np.array(getGameFrames(watcher, "na1", gameid))

model = tf.keras.models.load_model("model.model")

predictions = model.predict(data)

time = [item[0] for item in data]
output = [item[0] for item in predictions]

plt.ylim(0, 1)
plt.plot(time, output, color = "blue")
plt.plot(time, [.5]*len(time), color = "black")
plt.show()
