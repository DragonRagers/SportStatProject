from riotwatcher import RiotWatcher, ApiError


watcher = RiotWatcher("KEY") #API key
region = "na1"
gameid = 3026807896 #one of my recnt games

game = watcher.match.timeline_by_match(region, gameid)
print(game)
