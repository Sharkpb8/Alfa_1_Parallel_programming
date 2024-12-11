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
        
    
    