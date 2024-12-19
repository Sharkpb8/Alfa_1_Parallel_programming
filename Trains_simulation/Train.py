from DoublyLinkedList import *
import json
import asyncio

class Train():
    def __init__(self,type,train_number,speed,capacity,fuel,consumption,tracks):
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
        if(fuel<=0):
            raise ValueError
        if(consumption<=0):
            raise ValueError
        self.type = type
        self.train_number = train_number
        self.speed = speed
        self.capacity = capacity
        self.current_passangers = []
        self.fuel = fuel
        self.current_fuel = fuel
        self.consumption = consumption
        self.tracks = tracks
    
    def addstation(self,name,distance):
        self.tracks.addhead(name,distance)
    
    def removestation(self,name):
        self.tracks.remove(name)
    
    def getallstations(self):
        return self.tracks.FindAll()
    
    def gettrackssize(self):
        return self.tracks.get_size()
    
    def getcurrentfuel(self):
        return self.current_fuel
    
    def movetrain(self):
        return self.tracks.moveforward()
    
    def distancetonext(self):
        return self.tracks.nextdistance()
    
    def concat(self):
        return f"{self.type}{self.train_number}"
    
    def fuelneeded(self):
        return (self.current_fuel-self.distancetonext()*self.consumption)*-1
    
    def needrefill(self,travel):
        if(self.current_fuel-self.consumption*travel>0):
            return False
        else:
            return True
    
    def refuel(self,newfuel):
        self.current_fuel += newfuel

    def consumefuel(self,distance):
        self.current_fuel -= distance*self.consumption
    
    def trainposition(self):
        return {"current_station":self.tracks.current_station(),"direction":self.tracks.reverse}
    
    def addpassangers(self,passanger):
        if(len(self.current_passangers)+1>self.capacity):
            return True
        else:
            self.current_passangers.append(passanger)
            return False
    
    async def removepassanger(self,station,config,log,t):
        count =0
        for i in self.current_passangers[:]:
            if i == station:
                await asyncio.sleep(config["getoff-time"])
                self.current_passangers.remove(i)
                count +=1
        await log(f"Z vlaku vystoupilo {count} cestujících",t)
            
    
    def __str__(self):
        return f"Vlak: {self.type} {self.train_number} s rychlostí {self.speed}km/s kapacitou {self.capacity} lidí s nádrží {self.fuel}L a spotřebou {self.consumption}L/km {self.tracks}"
