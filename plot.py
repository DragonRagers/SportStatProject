import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from riotwatcher import RiotWatcher
from gameData import getGameFrames
import pickle
from sklearn.linear_model import LogisticRegression

gameid = 2988389854
#key = input("Enter Riot API key:")
key = "RGAPI-c0ac5943-5349-4396-9ac7-9d29a3458e09"
watcher = RiotWatcher(key)

data = getGameFrames(watcher, "na1", gameid)
time = [item[0] for item in data]

for i in range(len(data)):
    data[i] = data[i][1:]
data = np.array(data)

#data = np.array([[i] + [0]*19 for i in range(40)])
if False: #neural net or logit model
    model = tf.keras.models.load_model("model.model")
    predictions = model.predict(data)
    predictions = [p[0] for p in predictions]
else:
    logmodel = pickle.load(open("logmodel.p", "rb"))
    predictions = logmodel.predict(data)
    predictions = [int(i) for i in predictions]

t1 = [item for item in predictions]
t2 = [1-item for item in predictions]

plt.ylim(0, 1)
plt.xlabel("Time (minutes)")
plt.ylabel("Chance of Winning (%)")
plt.title("Chances of Winning vs Time")

plt.plot(time, [.5]*len(time), color = "black")
plt.plot(time, t1, color = "blue")
plt.plot(time, t2, color = "red")
plt.show()
