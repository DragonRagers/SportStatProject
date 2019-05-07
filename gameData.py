from riotwatcher import RiotWatcher, ApiError #https://github.com/pseudonym117/Riot-Watcher
from gameFrame import GameFrame

dragonDict = {
    "FIRE_DRAGON" : 0,
    "AIR_DRAGON" : 1,
    "EARTH_DRAGON" : 2,
    "WATER_DRAGON" : 3,
    "ELDER_DRAGON" : 4
}

numChamps = 175

def getGameFrames(watcher, region, gameid, display = False):
    game = watcher.match.timeline_by_match(region, gameid) #returns dictionary of game info
    #documentation of API here: https://developer.riotgames.com/api-methods/

    #print(game, "\n")
    #get list of all frames and create list of blank GameFrame's
    frames = game.get("frames")
    gameFrames = []
    for i in range(len(frames)):
        gameFrames.append(GameFrame(i))

    for i, frame in enumerate(frames):
        if display:
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
                experienceDifference -= player.get("xp")
        if display:
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
                    team = 0
                else: #red team destroyed blue building
                    team = 1

                #if it was a tower/turret
                if event.get("buildingType") == "TOWER_BUILDING":
                    for t in range(i,len(gameFrames)): #for frames from now to the end of the game
                        if team == 0:
                            gameFrames[t].turretDifference += 1 #if it was team 1 add to the difference
                        else:
                            gameFrames[t].turretDifference -= 1 #if it was team 2 subtract from the difference
                elif event.get("buildingType") == "INHIBITOR_BUILDING":
                    end = i+5 #inhibitors last for 5 minutes
                    if end > len(gameFrames):
                        end = len(gameFrames)
                    for t in range(i,end):
                        gameFrames[t].inhibsDestroyed[team] += 1

                if display:
                    print(event.get("buildingType"), "destroyed by Team ", team) #print building destroyed and by which team
                #100 = blue team, 200 = red team (based on testing)

            #on epic (elite) monster kill
            elif type == "ELITE_MONSTER_KILL":
                if event.get("killerId") <= 5: #if killed by someone on team 1
                    team = 0
                else: #else it was killed by team 2
                    team = 1

                monsterType = event.get("monsterType")
                #print(monsterType)
                if monsterType == "DRAGON": #if dragon
                    dragonType = dragonDict.get(event.get("monsterSubType")) #converts dragonType to an int, see dragonDict
                    if not dragonType == 4: #if not elder dragons
                        for t in range(i, len(gameFrames)): #add to the rest of the game
                            gameFrames[t].dragons[team*4 + dragonType] += 1 #plus one to the respective position
                    else:
                        end = i+2
                        if end > len(gameFrames):
                            end = len(gameFrames)
                        for t in range(i, end): #for the next 2 minutes
                            gameFrames[t].dragons[team*4 + dragonType] += 1

                    if display:
                        print(event.get("monsterSubType"), "slain by Team", team)  #print dragon type and team

                elif monsterType == "BARON_NASHOR": #if baron
                    end = i+3
                    if end > len(gameFrames):
                        end = len(gameFrames)
                    for t in range(i,end): #for the next 3 minutes
                        gameFrames[t].baron[team] = 1

                    if display:
                        print("BARON_NASHOR slain by Team", team) #print baron and team

                elif monsterType == "RIFTHERALD":
                    end = i+4
                    if end > len(gameFrames):
                        end = len(gameFrames)
                    for t in range(i,end):
                        gameFrames[t].rift[team] += 1

                    if display:
                        print("RIFT HERALD slain by Team", team)
    gameFramesAsArray = []
    for gF in gameFrames:
        gameFramesAsArray.append(gF.toArray())
    return gameFramesAsArray

def getGameInfo(watcher, region, gameid, display = False): #gets general game data i.e. who won
    game = watcher.match.by_id(region, gameid)
    if game.get("teams")[0].get("win") == "Win": #if the first team won
        if display:
            print("Team 0 Won")
        win = 1 #1 as in the first team won
    else:
        if display:
            print("Team 1 Won")
        win = 0 #0 as in first team lost

    #get champian ids
    players = game.get("participants")
    ally = [0] * numChamps
    enemy = [0] * numChamps
    for player in players:
        if player.get("teamId") == 100: #blue side
            ally[player.get("championId")] += 1
        else:
            enemy[player.get("championId")] += 1

    return win, ally + enemy

def generateData(watcher, region, gameid, display = False):
    win, champs = getGameInfo(watcher, region, gameid, display)
    return win, getGameFrames(watcher, region, gameid, display) #, champs

if __name__ == "__main__":
    #create RiotWatcher object and initialize some constants for testing
    key = input("Enter Riot API Key: ") #currently using development key, may apply for project key when project is actually working
    watcher = RiotWatcher(key)
    region = "na1"
    gameid = 3026756563 #3024748419 #one of my recent games

    gameFrameArrays = getGameFrames(watcher, region, gameid, True)
    for gFA in gameFrameArrays:
        print(gFA)

    getGameInfo(watcher, region, gameid)
