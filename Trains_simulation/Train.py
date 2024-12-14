from DoublyLinkedList import *
from Error import *
import json

class Train():
    def __init__(self,type,train_number,tracks):
        if(not isinstance(type,str)):
            raise ValueError
        with open("./Trains_simulation/config.json","r") as j:
            config = json.load(j)
            allowedtypes = config["allowedtypes"]
        if(type not in allowedtypes):
            raise ValueError
        if(not isinstance(train_number,int)):
            raise TypeError
        if(train_number < 1000 and train_number > 9999):
            raise LenghtError
        if(not isinstance(tracks,LinkedList)):
            raise TypeError
        self.type = type
        self.train_number = train_number
        self.tracks = tracks
    
    def __str__(self):
        return f"Vlak: {self.type} {self.train_number} ma zastavky NOT IMPLEMENTED"
