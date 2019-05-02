import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from riotwatcher import RiotWatcher
from gameData import getGameFrames

gameid = 3024748419
watcher = RiotWatcher("RGAPI-ce1e9b86-88e7-4efb-8ff0-4aa1df56abda")
data = np.array(getGameFrames(watcher, "na1", gameid))

model = tf.keras.models.load_model("model.model")

predictions = model.predict(data)

time = [item[0] for item in data]
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
