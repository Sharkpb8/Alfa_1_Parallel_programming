from Player import *
import asyncio

class Wizard(Player):
    def __init__(self, username):
        Player.__init__(self,username,70,"Wizard")
        self.fireballcooldown = 2
        self.Fireballdemage = 30
    
    async def Fireball(self):
        cooldown = self.fireballcooldown*(1-0.1*(self.level-1))
        print(cooldown)
        await asyncio.sleep(cooldown)
        return self.Fireballdemage
        
    
    