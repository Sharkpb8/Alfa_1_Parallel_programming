from DoublyLinkedList import *
import json
import asyncio

class Train():
    def __init__(self,type,train_number,speed,capacity,fuel,consumption,tracks):
        if(not isinstance(type,str)):
            raise TypeTypeError
        with open("./Trains_simulation/config.json","r") as j:
            config = json.load(j)
            allowedtypes = config["allowedtypes"]
        if(type not in allowedtypes):
            raise TrainTypeError
        if(not isinstance(train_number,int)):
            raise TrainNumberTypeError
        if(train_number < 1000 or train_number > 9999):
            raise TrainNumberLenghtError
        if(not isinstance(tracks,LinkedList)):
            raise TracksTypeError
        if(not isinstance(speed,int)):
            raise SpeedTypeError
        if(speed<=0):
            raise SpeedError
        if(not isinstance(capacity,int)):
            raise CapacityTypeError
        if(capacity<=0):
            raise CapacityError
        if(not isinstance(fuel,int)):
            raise FuelTypeError
        if(fuel<=0):
            raise FuelError
        if(not isinstance(consumption,int)):
            raise ConsumptionTypeError
        if(consumption<=0):
            raise ConsumptionError
        self.type = type
        self.train_number = train_number
        self.speed = speed
        self.capacity = capacity
        self.current_passangers = []
        self.fuel = fuel
        self.current_fuel = fuel
        self.consumption = consumption
        self.tracks = tracks
    
    def addstation(self,name = None,distance = None):
        if(name is None or distance is None):
            raise EmptyInputError
        self.tracks.addhead(name,distance)
    
    def removestation(self,name = None):
        if(name is None):
            raise EmptyInputError
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
    
    def needrefill(self,travel = None):
        if(travel is None):
            raise EmptyInputError
        if(isinstance(travel,bool)):
            raise TravelTypeError
        if(not isinstance(travel,int)):
            raise TravelTypeError
        if(self.current_fuel-self.consumption*travel>0):
            return False
        else:
            return True
    
    def refuel(self,newfuel = None):
        if(newfuel is None):
            raise EmptyInputError
        if(isinstance(newfuel,bool)):
            raise FuelTypeError
        if(not isinstance(newfuel,int)):
            raise FuelTypeError
        self.current_fuel += newfuel

    def consumefuel(self,distance):
        if(not isinstance(distance,int)):
            raise DistanceTypeError
        self.current_fuel -= distance*self.consumption
    
    def trainposition(self):
        return {"current_station":self.tracks.current_station(),"direction":self.tracks.reverse}
    
    def addpassangers(self,passanger):
        if(not isinstance(passanger,str)):
            raise PassangerTypeError
        if(len(self.current_passangers)+1>self.capacity):
            return True
        else:
            self.current_passangers.append(passanger)
            return False
    
    async def removepassanger(self,station,config,log,t):
        if(not isinstance(station,str)):
            raise DataTypeError
        if(not isinstance(t,Train)):
            raise TrainTypeError
        count =0
        for i in self.current_passangers[:]:
            if i == station:
                await asyncio.sleep(config["getoff-time"])
                self.current_passangers.remove(i)
                count +=1
        await log(f"Z vlaku vystoupilo {count} cestujících",t)
            
    
    def __str__(self):
        return f"Vlak: {self.type} {self.train_number} s rychlostí {self.speed}km/s kapacitou {self.capacity} lidí s nádrží {self.fuel}L a spotřebou {self.consumption}L/km {self.tracks}"
