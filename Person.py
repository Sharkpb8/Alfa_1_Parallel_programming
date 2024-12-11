class Person:
    def __init__(self,username,playerclass):
        if(not isinstance(username,str)):
            raise TypeError
        self.username = username
        self.playerclass = playerclass
        self.max_health = 100
        self.current_health = 100
        self.xp = 0

    def __str__(self):
        return f"Háč {self.username} má aktuálně {self.current_health} životu"

