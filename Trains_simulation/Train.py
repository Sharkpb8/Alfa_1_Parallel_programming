from DoublyLinkedList import *
import json
import asyncio

class Train():
    def __init__(self,type,train_number,speed,capacity,fuel,consumption,tracks):
        """
        Represents a train with attributes such as type, speed, capacity, fuel, and tracks.

        :param type: The type of train (based on `config.json`).
        :type type: str
        :param train_number: The train number (4-digit integer).
        :type train_number: int
        :param speed: The speed of the train in km/s.
        :type speed: int
        :param capacity: The maximum number of passengers the train can hold.
        :type capacity: int
        :param fuel: The total fuel capacity of the train.
        :type fuel: int
        :param consumption: The fuel consumption per kilometer.
        :type consumption: int
        :param tracks: A doubly linked list representing the train's tracks.
        :type tracks: LinkedList

        :raises TypeTypeError: If the train type is not a string.
        :raises TrainTypeError: If the train type is not allowed.
        :raises TrainNumberTypeError: If the train number is not an integer.
        :raises TrainNumberLenghtError: If the train number is not 4 digits.
        :raises TracksTypeError: If tracks is not a LinkedList.
        :raises SpeedTypeError: If speed is not an integer.
        :raises SpeedError: If speed is less than or equal to zero.
        :raises CapacityTypeError: If capacity is not an integer.
        :raises CapacityError: If capacity is less than or equal to zero.
        :raises FuelTypeError: If fuel is not an integer.
        :raises FuelError: If fuel is less than or equal to zero.
        :raises ConsumptionTypeError: If consumption is not an integer.
        :raises ConsumptionError: If consumption is less than or equal to zero.
        """
        if(not isinstance(type,str)):
            raise TypeTypeError
        with open("./Trains_simulation/config.json","r") as j:
            config = json.load(j)
            allowedtypes = config["allowedtypes"]
        if(type not in allowedtypes):
            raise TrainTypeError
        if(not isinstance(train_number,int)):
            raise TrainNumberTypeError
        if(isinstance(train_number,bool)):
            raise TrainNumberTypeError
        if(train_number < 1000 or train_number > 9999):
            raise TrainNumberLenghtError
        if(not isinstance(tracks,LinkedList)):
            raise TracksTypeError
        if(not isinstance(speed,int)):
            raise SpeedTypeError
        if(isinstance(speed,bool)):
            raise SpeedTypeError
        if(speed<=0):
            raise SpeedError
        if(not isinstance(capacity,int)):
            raise CapacityTypeError
        if(isinstance(capacity,bool)):
            raise CapacityTypeError
        if(capacity<=0):
            raise CapacityError
        if(not isinstance(fuel,int)):
            raise FuelTypeError
        if(isinstance(fuel,bool)):
            raise FuelTypeError
        if(fuel<=0):
            raise FuelError
        if(not isinstance(consumption,int)):
            raise ConsumptionTypeError
        if(isinstance(consumption,bool)):
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
        """
        Adds a station to the tracks.

        :param name: The name of the station.
        :type name: str
        :param distance: The distance from the previous station.
        :type distance: int

        :raises EmptyInputError: If name or distance is None.
        """
        if(name is None or distance is None):
            raise EmptyInputError
        if(not self.isreachable(distance)):
            raise NotReachableStationError
        self.tracks.addhead(name,distance)
    
    def removestation(self,name = None):
        """
        Removes a station by its name.

        :param name: The name of the station to remove.
        :type name: str

        :raises EmptyInputError: If name is None.
        """
        if(name is None):
            raise EmptyInputError
        self.tracks.remove(name)
    
    def getallstations(self):
        """
        Retrieves all stations on the tracks.

        :return: A list of station names.
        :rtype: list[str]
        """
        return self.tracks.FindAll()
    
    def gettrackssize(self):
        """
        Retrieves the number of stations on the tracks.

        :return: The size of the tracks.
        :rtype: int
        """
        return self.tracks.get_size()
    
    def getcurrentfuel(self):
        """
        Retrieves the current fuel level.

        :return: The current fuel level.
        :rtype: int
        """
        return self.current_fuel
    
    def movetrain(self):
        """
        Moves the train to the next station.

        :return: A dictionary containing information about the move.
        :return: `from` - position from which the pointer moved.
        :rtype: str
        :return: `to` - position where the pointer is now.
        :rtype: str
        :return: `distance` distance from the original position to new
        :rtype: int
        :return: `finish` True if its the final destination otherwise False
        :rtype: bool
        :rtype: dict
        """
        return self.tracks.moveforward()
    
    def distancetonext(self):
        """
        Retrieves the distance to the next station.

        :return: The distance to the next station.
        :rtype: int
        """
        return self.tracks.nextdistance()
    
    def concat(self):
        """
        Concatenates the train type and number into a single string.

        :return: The concatenated train identifier.
        :rtype: str
        """
        return f"{self.type}{self.train_number}"
    
    def fuelneeded(self):
        """
        Calculates the fuel needed for the next trip.

        :return: The fuel deficit for the next trip.
        :rtype: int
        """
        return (self.current_fuel-self.distancetonext()*self.consumption)*-1
    
    def needrefill(self,travel = None):
        """
        Checks if the train needs a fuel refill for a given distance.

        :param travel: The distance to travel.
        :type travel: int

        :return: True if a refill is needed, False otherwise.
        :rtype: bool

        :raises EmptyInputError: If travel is None.
        :raises TravelTypeError: If travel is not an integer.
        """
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
        """
        Refuels the train with a given amount.

        :param newfuel: The amount of fuel to add.
        :type newfuel: int

        :raises EmptyInputError: If newfuel is None.
        :raises FuelTypeError: If newfuel is not an integer.
        """
        if(newfuel is None):
            raise EmptyInputError
        if(isinstance(newfuel,bool)):
            raise FuelTypeError
        if(not isinstance(newfuel,int)):
            raise FuelTypeError
        self.current_fuel += newfuel

    def consumefuel(self,distance = None):
        """
        Consumes fuel for a given distance.

        :param distance: The distance traveled.
        :type distance: int

        :raises EmptyInputError: If distance is None.
        :raises DistanceTypeError: If distance is not an integer.
        :raises LowFuelError: If there is insufficient fuel.
        """
        if(distance is None):
            raise EmptyInputError
        if(isinstance(distance,bool)):
            raise DistanceTypeError
        if(not isinstance(distance,int)):
            raise DistanceTypeError
        if(self.current_fuel - distance*self.consumption<0):
            raise LowFuelError
        else:
            self.current_fuel -= distance*self.consumption
    
    def trainposition(self):
        """
        Retrieves the train's current position and direction.

        :return: A dictionary with the current station and direction.
        :rtype: dict
        """
        return {"current_station":self.tracks.current_station(),"direction":self.tracks.reverse}
    
    def addpassangers(self,passanger = None):
        """
        Adds a passenger to the train.

        :param passanger: Name of destination for passanger.
        :type passanger: str

        :return: True if the train is at capacity, False otherwise.
        :rtype: bool

        :raises EmptyInputError: If passanger is None.
        :raises PassangerTypeError: If passanger is not a string.
        """
        if(passanger is None):
            raise EmptyInputError
        if(isinstance(passanger,bool)):
            raise PassangerTypeError
        if(not isinstance(passanger,str)):
            raise PassangerTypeError
        if(len(self.current_passangers)+1>self.capacity):
            return True
        else:
            self.current_passangers.append(passanger)
            return False
    
    async def removepassanger(self,station,config,log,t):
        """
        Removes passengers at a given station asynchronously.

        :param station: The station name.
        :type station: str
        :param config: Configuration dictionary for timing.
        :type config: dict
        :param log: Logging function for recording actions.
        :type log: Callable
        :param t: The train object for context.
        :type t: Train

        :raises EmptyInputError: If station is None.
        :raises DataTypeError: If station is not a string.
        :raises TrainTypeError: If t is not a Train instance.
        """
        if(station is None):
            raise EmptyInputError
        if(isinstance(station,bool)):
            raise PassangerTypeError
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
    
    def isreachable(self,travel):
        """
        Determines whether a station is possible to reach with the maximum fuel level and the fuel consumption rate.

        :param travel: The distance to be traveled.
        :type travel:int
        :return: True if reachable, False if not.
        :rtype: bool
        """
        if(self.fuel -travel*self.consumption<0):
            return False
        else:
            return True
    
    def __str__(self):
        """
        Returns a string representation of the train.

        :return: A string describing the train.
        :rtype: str
        """
        return f"Vlak: {self.type} {self.train_number} s rychlostí {self.speed}km/s kapacitou {self.capacity} lidí s nádrží {self.fuel}L a spotřebou {self.consumption}L/km {self.tracks}"
