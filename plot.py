import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from riotwatcher import RiotWatcher
from gameData import getGameFrames
import pickle
from sklearn.linear_model import LogisticRegression
from generateData import getGameIdsBySummonerNames


def plotByGameId(watcher, region, gameid, type = 0):
    data = getGameFrames(watcher, region, gameid)
    time = [item[0] for item in data]

    for i in range(len(data)):
        data[i] = data[i][1:]
    data = np.array(data)

    #data = np.array([[i] + [0]*19 for i in range(40)])
    if type == 0: #neural net or logit model
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


def plotBySummonerName(watcher, region, name, type = 0):
    queues = [400, 420, 430, 440, 450]
    gameId = getGameIdsBySummonerNames(watcher, region, [name], queues)[0][1][0] #gets first gameId from that player
    print(gameId)
    plotByGameId(watcher, region, gameId, type)

def main():

    #key = input("Enter Riot API key:")
    key = "RGAPI-8c6e3728-5b5d-45ff-8a82-07bf31d468ea"
    w = RiotWatcher(key)
    r = "na1"
    g = 3036487185
    #plotByGameId(w,  r, g, 0)
    plotBySummonerName(w, r, "DragonRagers", 0)


if __name__ == "__main__":
    main()
