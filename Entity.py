class Entity:
    def __init__(self,name,max_health):
        if(not isinstance(name,str)):
            raise TypeError
        self.name = name
        if(not isinstance(max_health,int) or max_health <= 0):
            raise ValueError
        if(max_health):
            self.max_health = max_health
        else:
            self.max_health = 100
        self.current_health = self.max_health

