import os
import csv
from sklearn.linear_model import LogisticRegression
import pickle
import time


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

    for t, d in enumerate(minuteData):
        wins = []
        frames = []
        for f in d:
            wins.append(f[0])
            frames.append(f[1])

        x_train,y_train = frames, wins

        logmodel = LogisticRegression()
        logmodel.fit(x_train,y_train)

        out = pickle.dump(logmodel, open("logit/logmodel{}.p".format(t), "wb"))


def main():
    trainModel()


if __name__ == "__main__":
    main()
