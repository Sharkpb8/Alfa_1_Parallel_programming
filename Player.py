from Entity import *

class Player(Entity):
    def __init__(self,username,max_health,playerclass):
        self.playerclass = playerclass
        # self.xp = 0
        Entity.__init__(self,username,max_health)
    
    def __str__(self):
        if(self.current_health <=0):
            return f"Hráč {self.name} je mrtvý"
        else:
            return f"Hráč {self.name} má {self.current_health} životů"