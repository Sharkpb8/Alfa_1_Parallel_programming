from Entity import *

class Player(Entity):
    def __init__(self,username,max_health,playerclass):
        Entity.__init__(self,username,max_health)
        if(not isinstance(playerclass,str)):
            raise TypeError
        self.playerclass = playerclass
        self.xp = 0
        self.level = 1

    def addxp(self,ammount):
        if(not isinstance(ammount,int)):
            raise TypeError
        if(ammount <0):
            raise ValueError
        if(self.xp+ammount >=1000):
            self.level +=1
            self.max_health *= 1.1
            self.xp += ammount-1000
        else:
            self.xp +=ammount 
    
    def __str__(self):
        if(self.current_health <=0):
            return f"Hráč {self.name} je mrtvý"
        else:
            return f"Hráč {self.name} má {self.current_health} životů"