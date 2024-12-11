import asyncio

class Enemy:
    def __init__(self,hp,demage):
        self.hp = hp
        self.demage = demage
    
    async def attack(self):
        await asyncio.sleep(1)
        return self.demage
    
    async def takedemage(self,demage):
        self.hp -= demage
    
    def current_hp(self):
        if(self.hp <=0):
            return f"enemy je mrtvý"
        else:
            return f"enemy má {self.hp}"