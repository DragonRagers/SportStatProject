#to be an object holding relevent game info at a  certain timeline_by_match
#relevent game data being what is going to be used in the model
class GameFrame:

    def __init__(self, time):
        #0 and 1 used in place of True and False for later model training
        #in game time in minutes
        self.time = time

        #list where index 1 = ally baron active, 2 = enemy baron active
        self.baron = [0,0]

        #list dragon buffs, index is type (including elder) and value is number of dragons taken. First 5 would be ally and later 5 would be enemy
        self.dragons = [0,0,0,0,0, 0,0,0,0,0] #ie [1,0,0...] could mean team 1 has one infernal dragon

         #difference in team expereience (unit to level conversion can likely be found on a wiki)
        self.xpDifference = 0

        #current team gold differentials
        self.goldDifference = 0

        #difference in turrets destroyed
        self.turretDifference = 0

        #"tuple" for number each team has destoryed
        self.inhibsDestroyed = [0,0]

    def toArray(self):
        return [self.time] + self.baron + self.dragons + [self.xpDifference, self.goldDifference, self.turretDifference] + self.inhibsDestroyed
