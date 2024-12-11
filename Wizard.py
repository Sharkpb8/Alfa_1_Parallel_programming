from Player import *
import asyncio

class Wizard(Player):
    def __init__(self, username):
        Player.__init__(self,username,70,"Wizard")
        self.fireballcooldown = 1
        self.Fireballdemage = 30
    
    async def Fireball(self):
        await asyncio.sleep(2*self.fireballcooldown)
        return self.Fireballdemage
    
    async def takedemage(self,demage):
        self.current_health -= demage
    
    def current_hp(self):
        if(self.current_health <=0):
            return f"hráč je mrtvý"
        else:
            return f"hráč má {self.current_health}"
    
    