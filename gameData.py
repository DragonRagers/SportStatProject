from riotwatcher import RiotWatcher, ApiError #https://github.com/pseudonym117/Riot-Watcher
from gameFrame import GameFrame

#create RiotWatcher object and initialize some constants for testing
key = input("Enter Riot API Key: ") #currently using development key, may apply for project key when project is actually working
watcher = RiotWatcher(key)
region = "na1"
gameid = 3024748419 #one of my recent games

game = watcher.match.timeline_by_match(region, gameid) #returns dictionary of game info
#documentation of API here: https://developer.riotgames.com/api-methods/


#print(game, "\n")
#get list of all frames and create list of blank GameFrame's
frames = game.get("frames")
gameFrames = []
for i in range(len(frames)):
    gameFrames.append(GameFrame(i))

for i, frame in enumerate(frames):
    print("\nMinute:", i) #where i analogous to in game minutes

    #calculates gold and experience difference
    goldDifference = 0
    experienceDifference = 0
    participantFrames = frame.get("participantFrames")
    #print(participantFrames)
    for p in range(1,11): #for every player (assuming 10)
        player = participantFrames.get(str(p))
        if player.get("participantId") <= 5: #if player on team 1
            team = True
        else: #else player on team 2
            team = False

        if team: #if on team 1 add to the goldDifference and experienceDifference
            goldDifference += player.get("totalGold")
            experienceDifference += player.get("xp")
        else: #if on team 2 subtract fom goldDifference and experienceDifference
            goldDifference -= player.get("totalGold")
            experienceDifference += player.get("xp")
    print("Gold Difference:", goldDifference)
    print("Experience Difference:", experienceDifference)
    gameFrames[i].goldDifference = goldDifference
    gameFrames[i].xpDifference = experienceDifference

    #prints objective kills (towers, inhibs, dragons, barons)
    events = frame.get("events")
    for event in events:
        #on building kill
        type = event.get("type")
        if type == "BUILDING_KILL":
            if event.get("teamId") == 200: #blue destroyed red building
                team = 1
            else: #red team destroyed blue building
                team = 2

            #if it was a tower/turret
            if event.get("buildingType") == "TOWER_BUILDING":
                for t in range(i,len(gameFrames)): #for frames from now to the end of the game
                    if team == 1:
                        gameFrames[t].turretDifference += 1 #if it was team 1 add to the difference
                    else:
                        gameFrames[t].turretDifference -= 1 #if it was team 2 subtract from the difference

            print(event.get("buildingType"), "destroyed by Team ", team) #print building destroyed and by which team
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

for gF in gameFrames:
    print(gF.toArray())
