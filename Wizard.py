from Person import *
import asyncio

class Wizard(Person):
    def __init__(self, username):
        Person().__init__(username,"Wizard")
        self.fireballcooldown = 1
        self.Fireballdemage = 10
    
    async def Fireball(self):
        await asyncio.sleep(2*self.fireballcooldown)
        return self.Fireballdemage
    
    
    