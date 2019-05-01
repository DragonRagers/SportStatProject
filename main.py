from riotwatcher import RiotWatcher
from gameData import generateData
import time
import csv

queues = [400, 420, 440] #codes for relevent queues: https://developer.riotgames.com/game-constants.html

def unpack(data):
    unpackedWins = []
    unpackedFrames = []
    for frame in data[1]:
        unpackedWins.append(data[0])
        unpackedFrames.append(frame)
    return unpackedWins, unpackedFrames

def generateDataByGameIds(watcher, region, gameIds, queue = queues):
    wins = []
    frames = []
    for i, gameId in enumerate(gameIds):
        print("Working on game", i, "of", len(gameIds))
        data = generateData(watcher, region, gameId)
        w, f = unpack(data)
        wins += w
        frames += f

    fileName = "data{}.csv".format(time.time())
    file = open(fileName,'w',newline='')
    writer = csv.writer(file, delimiter = ",")
    writer.writerow(["Team 0 Win", "Time", "AllyBaron", "EnemyBaron", "AllyInfernal", "AllyAir", "AllyEarth", "AllyWater", "AllyElder", "EnemyInfernal",
     "EnemyAir", "EnemyEarth", "EnemyWater", "EnemyElder", "XpDiff", "GoldDiff", "TurretDiff", "AllyInhibs", "EnemyInhibs"])
    for i in range(len(wins)):
        writer.writerow([wins[i]] + frames[i])
    print("File saved as:", fileName)


def getGameIdsBySummonerName(watcher, region, name):
    matchIds = []
    id = watcher.summoner.by_name(region, name).get("accountId")
    matches = watcher.match.matchlist_by_account(region, id).get("matches")
    #print(matches)

    for match in matches:
        matchIds.append(match.get("gameId"))
    return matchIds


def main():
    key = input("Enter Riot API Key: ") #currently using development key, may apply for project key when project is actually working
    w = RiotWatcher(key)
    r = "na1"

    g = getGameIdsBySummonerName(w, r, "DragonRagers") #3024748419 #one of my recent games
    #g = g[:10]
    generateDataByGameIds(w, r, g)


if __name__ == "__main__":
    main()
