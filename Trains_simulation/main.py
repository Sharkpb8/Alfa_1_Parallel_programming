from Train import *
from Error import *
import json

def openjson():
    with open('./Trains_simulation/config.json', 'r') as j:
        config = json.load(j)
        return config

def showoptions(list):
    count =1
    for i in list:
        print(f"{count}. {i}")
        count +=1

def addtrain():
    config = openjson()
    allowedtypes = config["allowedtypes"]
    optionpicked = False
    newtrain = {"type":None,"train_number":None}
    while not optionpicked:
        print("Vyber si typ")
        showoptions(allowedtypes)
        choice = input("Vybírám si: ")
        try:
            numberchoise = int(choice)
            newtrain["type"] = allowedtypes[numberchoise-1]
            break
        except ValueError:
            if(choice in allowedtypes):
                newtrain["type"] = choice
                break
        print("Špatná volba")
    
    while not optionpicked:
        print("Vybere 4 místné číslo vlaku")
        choice = input("Vybírám si: ")
        try:
            numberchoise = int(choice)
            if(numberchoise < 1000 or numberchoise > 9999):
                raise LenghtError
            newtrain["train_number"] = numberchoise
            break
        except ValueError:
            print("Zvolte číslo")
        except LenghtError:
            print("Číslo musí být 4 ciferne")
    t = Train(newtrain["type"],newtrain["train_number"],LinkedList())
    return t

        
    

running = True
trainlist = []
while running:
    options = ["Pridat vlak","Vypis valku","Ukončit"]
    showoptions(options)
    choice = input("Vybírám si: ")
    match choice:
        case "Pridat vlak" | "1":
            t = addtrain()
            trainlist.append(t)
        case "Vypis valku" | "2":
            if(len(trainlist) == 0):
                print("Žádny vlaky nebyly vytvořeny")
            else:
                for i in trainlist:
                    print(i)
        case "Ukončit" | "3":
            running = False
        case _:
            print("Špatná volba")
