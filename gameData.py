#https://github.com/pseudonym117/Riot-Watcher
from riotwatcher import RiotWatcher, ApiError
import GameFrame

#create RiotWatcher object and initialize some constants for testing
key = input("Enter Riot API Key: ") #currently using development key, may apply for project key when project is actually working
watcher = RiotWatcher(key)
region = "na1"
gameid = 3024748419 #one of my recent games

game = watcher.match.timeline_by_match(region, gameid) #returns dictionary of game info
#documentation of API here: https://developer.riotgames.com/api-methods/

#print(game, "\n")
frames = game.get("frames")
for i, frame in enumerate(frames):
    print("Frame: ", i)
    events = frame.get("events")
    for event in events:
        #on building kill
        if event.get("type") == "BUILDING_KILL":
            print(event.get("buildingType"), "Team ", event.get("teamId")) #print building destroyed and by which team
            #100 = blue team, 200 = red team (based on testing)

        #on epic (elite) monster kill
        elif event.get("type") == "ELITE_MONSTER_KILL":
            if event.get("monsterType") == "DRAGON": #if dragon
                print(event.get("monsterSubType"))  #print dragon type

            elif event.get("monsterType") == "BARON_NASHOR": #if baron
                print("Baron Nashor") #print baron

            if event.get("killerId") <= 5: #if killed by someone on team 1
                print("by Team 1")
            else: #else it was killed by team 2
                print("by Team 2")
