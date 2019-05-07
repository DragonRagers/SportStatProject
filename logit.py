import os
import csv
from sklearn.linear_model import LogisticRegression
import pickle


def appendData(): #don't actually need this
    out = open("data/data.csv","w")

    fileNames = []
    for fileName in os.listdir("data"):
        fileNames.append(fileName)

    for name in fileNames:
        f = open("data/" + name)
        for line in f:
             out.write(line)
        print("Added", name)
        f.close()
    out.close()


def trainModel():
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

    for d in data:
        wins.append(d[0])
        frames.append(d[2:]) #ignores who won and time
    x_train,y_train = frames, wins  #np.array(frames), np.array(wins)

    logmodel = LogisticRegression()
    logmodel.fit(x_train,y_train)

    out = pickle.dump(logmodel, open("logmodel.p", "wb"))


def main():
    trainModel()


if __name__ == "__main__":
    main()
