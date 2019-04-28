#https://github.com/pseudonym117/Riot-Watcher
from riotwatcher import RiotWatcher, ApiError

#create RiotWatcher object and initialize some constants for testing
key = input("Enter Riot API Key: ") #currently using development key, may apply for project key when project is actually working
watcher = RiotWatcher(key)
region = "na1"
gameid = 3026807896 #one of my recent games

game = watcher.match.timeline_by_match(region, gameid) #returns dictionary of game info
#documentation of API here: https://developer.riotgames.com/api-methods/

#print(game, "\n")
numFrames = len(game.get("frames"))
for i in range(numFrames):
    print("Frame: ", i)
    events = game.get("frames")[i].get("events")
    for event in events:
        if event.get("type") == "BUILDING_KILL":
            print(event.get("buildingType"))
