#to be an object holding relevent game info at a  certain timeline_by_match
#relevent game data being what is going to be used in the model
class GameFrame:

    def __init__(self, time):
        #0 and 1 used in place of True and False for later model training
        #in game time in minutes
        self.time = time

        #list where index 0 = no baron active, 1 = ally baron active, 2 = enemy baron active
        self.baron = [0,0,0]

        #list dragon buffs, index is type and value is number of dragons taken. First 4 would be ally and later 4 would be enemy
        self.dragons = [0,0,0,0, 0,0,0,0] #ie [1,0,0...] could mean team 1 has one infernal dragon

         #difference in team expereience (unit to level conversion can likely be found on a wiki)
        self.xpDifference = None

        #current team gold differentials
        self.goldDifference = None

        #TBD: either differential or tuple for number destroyed per team
        self.turretDestroyed = None

        #tuple for number each team has destoryed
        self.inhibsDestroyed = None

    def toArray(self):
        return [self.time] + self.baron + self.dragons + [self.xpDifference, self.goldDifference, self.turretDestroyed, self.inhibsDestroyed]
