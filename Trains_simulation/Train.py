from DoublyLinkedList import *
from Error import *
import json

class Train():
    def __init__(self,type,train_number,speed,capacity,tracks):
        if(not isinstance(type,str)):
            raise ValueError
        with open("./Trains_simulation/config.json","r") as j:
            config = json.load(j)
            allowedtypes = config["allowedtypes"]
        if(type not in allowedtypes):
            raise TrainTypeError
        if(not isinstance(train_number,int)):
            raise TypeError
        if(train_number < 1000 and train_number > 9999):
            raise LenghtError
        if(not isinstance(tracks,LinkedList)):
            raise TypeError
        if(not isinstance(speed,int)):
            raise TypeError
        if(speed<=0):
            raise SpeedError
        if(not isinstance(capacity,int)):
            raise TypeError
        if(capacity<=0):
            raise CapacityError
        self.type = type
        self.train_number = train_number
        self.speed = speed
        self.capacity = capacity
        self.current_passangers = []
        self.tracks = tracks
    
    def addstation(self,name,distance):
        self.tracks.addhead(name,distance)
    
    def removestation(self,name):
        self.tracks.remove(name)
    
    def getallstations(self):
        return self.tracks.FindAll()
    
    def gettrackssize(self):
        return self.tracks.get_size()
    
    def movetrain(self):
        return self.tracks.moveforward()
    
    def trainposition(self):
        return {"current_station":self.tracks.current_station(),"direction":self.tracks.reverse}
    
    def addpassangers(self,passanger):
        if(len(self.current_passangers)+1>self.capacity):
            return True
        else:
            self.current_passangers.append(passanger)
            return False
    
    def __str__(self):
        return f"Vlak: {self.type} {self.train_number} s rychlostí {self.speed}km/s {self.tracks}"
