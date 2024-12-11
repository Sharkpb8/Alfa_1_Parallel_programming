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
    
    def __str__(self):
        if(self.current_health <= 0):
            return f"Nepřítel {self.name} je mrtvý"
        else:
            return f"Nepřítel {self.name} má {self.current_health} životů"