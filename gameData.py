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
    print("\nMinute:", i) #where i analogous to in game minutes

    goldDifference = 0
    participantFrames = frame.get("participantFrames")
    #print(participantFrames)
    for i in range(1,11): #for every player (assuming 10)
        player = participantFrames.get(str(i))
        if player.get("participantId") <= 5: #if player on team 1
            team = True
        else: #else player on team 2
            team = False

        if team: #if on team 1 add to the goldDifference
            goldDifference += player.get("totalGold")
        else: #if on team 2 subtract fom goldDifference
            goldDifference -= player.get("totalGold")
    print("Gold Difference:", goldDifference)


    events = frame.get("events")
    for event in events:
        #on building kill
        type = event.get("type")
        if type == "BUILDING_KILL":
            print(event.get("buildingType"), "Team ", event.get("teamId")) #print building destroyed and by which team
            #100 = blue team, 200 = red team (based on testing)

        #on epic (elite) monster kill
        elif type == "ELITE_MONSTER_KILL":
            if event.get("killerId") <= 5: #if killed by someone on team 1
                team = 1
            else: #else it was killed by team 2
                team = 2

            monsterType = event.get("monsterType")
            if monsterType == "DRAGON": #if dragon
                print(event.get("monsterSubType"), "slain by Team", team)  #print dragon type and team

            elif monsterType == "BARON_NASHOR": #if baron
                print("BARON_NASHOR slain by Team", team) #print baron and team
