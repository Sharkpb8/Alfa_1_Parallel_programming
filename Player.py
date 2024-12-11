from Entity import *

class Player(Entity):
    def __init__(self,username,max_health,playerclass):
        self.playerclass = playerclass
        # self.xp = 0
        Entity.__init__(self,username,max_health)