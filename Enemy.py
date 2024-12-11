import asyncio
from Entity import *

class Enemy(Entity):
    def __init__(self,name,max_health,demage):
        Entity.__init__(self,name,max_health)
        self.demage = demage
    
    async def attack(self):
        await asyncio.sleep(1)
        return self.demage
    
    async def takedemage(self,demage):
        self.current_health -= demage
    
    def current_hp(self):
        if(self.current_health <=0):
            return f"enemy je mrtvý"
        else:
            return f"enemy má {self.current_health}"