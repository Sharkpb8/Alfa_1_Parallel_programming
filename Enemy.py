class Enemy:
    def __init__(self,hp,demage):
        self.hp = hp
        self.demage = demage
    
    def attack(self):
        return self.demage
    
    def takedemage(self,demage):
        self.hp -= demage