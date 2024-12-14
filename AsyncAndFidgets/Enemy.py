import asyncio
from Entity import *
import random

class Enemy(Entity):
    def __init__(self,name,max_health,demage):
        Entity.__init__(self,name,max_health)
        if(not isinstance(demage,int)):
            raise TypeError
        if(demage<1):
            raise ValueError
        self.demage = demage
        self.xpgained = random.randint(250,800)
    
    async def attack(self):
        await asyncio.sleep(1)
        return self.demage
    
    def __str__(self):
        if(self.current_health <= 0):
            return f"Nepřítel {self.name} je mrtvý"
        else:
            return f"Nepřítel {self.name} má {self.current_health} životů"