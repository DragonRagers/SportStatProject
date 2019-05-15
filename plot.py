import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from riotwatcher import RiotWatcher
from gameData import getGameFrames
import pickle
from sklearn.linear_model import LogisticRegression
from generateData import getGameIdsBySummonerNames


def unconfidence(i):
    return (i - .5) ** 3 * 4 + .5

def plotByGameId(watcher, region, gameid, type = 0):
    data = getGameFrames(watcher, region, gameid)
    time = [item[0] for item in data]

    for i in range(len(data)):
        data[i] = data[i][1:]
    data = np.array(data)

    #data = np.array([[i] + [0]*19 for i in range(40)])
    predictions = []
    if type == 0: #neural net or logit model
        for i,d in enumerate(data):
            model = tf.keras.models.load_model("nn/model{}.model".format(i))
            predictions.append(model.predict(np.array([d]))[0])
    else:
        for i,d in enumerate(data):
            logmodel = pickle.load(open("logit/logmodel{}.p".format(i), "rb"))
            predictions.append(float(logmodel.predict([d])[0]))


    #artificially makes the confidence lower
    #predictions = [unconfidence(item) for item in predictions]

    t1 = [item for item in predictions]
    t2 = [1 - item for item in t1]

    plt.ylim(0, 1)
    plt.xlabel("Time (minutes)")
    plt.ylabel("Chance of Winning (%)")
    plt.title("Chances of Winning vs Time")

    plt.plot(time, [.5]*len(time), color = "black")
    plt.plot(time, t1, color = "blue")
    plt.plot(time, t2, color = "red")
    plt.show()


def plotBySummonerName(watcher, region, name, type = 0):
    queues = [400, 420, 430, 440, 450]
    gameId = getGameIdsBySummonerNames(watcher, region, [name], queues)[0][1][0] #gets first gameId from that player
    print(gameId)
    plotByGameId(watcher, region, gameId, type)

def main():

    #key = input("Enter Riot API key:")
    key = "RGAPI-69e9cbd7-035f-465f-8cc1-d1826272e5dc"
    w = RiotWatcher(key)
    r = "na1"
    g = 3040961431
    #plotByGameId(w,  r, g, 0)
    plotBySummonerName(w, r, "dragonragers", 0)


if __name__ == "__main__":
    main()
