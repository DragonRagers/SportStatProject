
#to be an object holding relevent game info at a  certain timeline_by_match
#relevent game data being what is going to be used in the model
class GameFrame:

    def __init__(self, time):
        self.time = time #in game time in minutes
        self.baron = None #where 0 = no baron active, 1 = ally baron active, 2 = enemy baron active
        self.dragons = None #list dragon buffs, index is type and value is number of dragons taken. First 4 would be ally and later 4 would be enemy
        self.xpDifference = None #difference in team expereience
        self.goldDifference = None #current team gold differentials
        self.turretDestroyed = None #TBD: either differential or tuple for number destroyed per team
        self.inhibsDestroyed = None #tuple for number each team has destoryed
