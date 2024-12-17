from Train import *
from Error import *
from simulation import *
import json
import asyncio

def openjson():
    with open('./Trains_simulation/config.json', 'r') as j:
        config = json.load(j)
        return config

def showoptions(list):
    count =1
    for i in list:
        print(f"{count}. {i}")
        count +=1

def showotrainptions(trainlist):
    count =1
    for i in trainlist:
        print(f"{count}. {trainlist[count-1].type}{trainlist[count-1].train_number}")
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


def addstation(trainlist):
    optionpicked = False
    while not optionpicked:
        print("Pro který vlak chce přidat stanici ?")
        showotrainptions(trainlist)
        choice = input("Vybírám si: ")
        try:
            numberchoise = int(choice)
            t = trainlist[numberchoise-1]
            station = input("Jmeno zastavky: ")
            t.addstation(station)
            break
        except ValueError:
            temptrainlist = []
            showotrainptions(trainlist)
            count = 0
            for i in temptrainlist:
                if(choice == i):
                    t = trainlist[count]
                    station = input("Jmeno zastavky: ")
                    t.addstation(station)
                    optionpicked = True
                else:
                    count +=1
            # print("dej tam cislo jsem linej to tet implementovat")
        if(not optionpicked):
            print("Špatná volba")

def deletetrain(trainlist):
    optionpicked = False
    while not optionpicked:
        print("Který vlak chcete smazat?")
        showotrainptions(trainlist)
        choice = input("Vybírám si: ")
        try:
            numberchoise = int(choice)
            del trainlist[numberchoise-1]
            return trainlist
        except ValueError:
            temptrainlist = []
            count = 0
            for i in trainlist:
                temptrainlist.append(f"{trainlist[count-1].type}{trainlist[count-1].train_number}")
                count +=1
            count = 0
            for i in temptrainlist:
                if(choice == i):
                    del trainlist[count]
                    return trainlist
                else:
                    count +=1
            # print("dej tam cislo jsem linej to tet implementovat")
        print("Špatná volba")
    
def removestation(trainlist):
    optionpicked = False
    while not optionpicked:
        print("Pro který vlak chce smazat stanici ?")
        showotrainptions(trainlist)
        choice = input("Vybírám si: ")
        try:
            numberchoise = int(choice)
            t = trainlist[numberchoise-1]
            stations = t.getallstations()
            showoptions(stations)
            choice = input("Vybírám si: ")
            try:
                numberchoise = int(choice)
                t.removestation(stations[numberchoise-1])
                break
            except ValueError:
                if(choice in stations):
                    t.removestation(choice)
                    break
        except ValueError:
            temptrainlist = []
            count = 0
            for i in trainlist:
                temptrainlist.append(f"{trainlist[count-1].type}{trainlist[count-1].train_number}")
                count +=1
            count = 0
            for i in temptrainlist:
                if(choice == i):
                    t = trainlist[count]
                    stations = t.getallstations()
                    showoptions(stations)
                    choice = input("Vybírám si: ")
                    try:
                        numberchoise = int(choice)
                        t.removestation(stations[numberchoise-1])
                        optionpicked = True
                        break
                    except ValueError:
                        if(choice in stations):
                            t.removestation(choice)
                            optionpicked = True
                            break
                else:
                    count +=1
            # print("dej tam cislo jsem linej to tet implementovat")
        if(not optionpicked):
            print("Špatná volba")

def load(trainlist):
    try:
        with open("./Trains_simulation/trains.json","r",encoding="utf-8") as j:
            loadlist = json.load(j)
            if(len(loadlist) == 0):
                return print("V souboru trains.json se nic nenachází")
            for i in loadlist:
                if("typ_vlaku"not in i or "cislo_vlaku" not in i or "rychlost" not in i or "kapacita" not in i):
                    raise FormatError
                if("typ_vlaku"not in i or "cislo_vlaku" not in i):
                    raise FormatError
                if("typ_vlaku"not in i or "cislo_vlaku" not in i):
                    raise FormatError
                if("stanice" not in i or not isinstance(i["stanice"], list)):
                    raise FormatError
                try:
                    t = Train(i["typ_vlaku"],i["cislo_vlaku"],i["rychlost"],i["kapacita"],i["nadrz"],i["spotreba"],LinkedList())
                except LenghtError:
                    print("Některý z vlaků má špatný číslo vlaku")
                except TrainTypeError:
                    print("Některý z vlaků má špatný typ")
                except ValueError:
                    print("Typ valku musí být písmena")
                except TypeError:
                    print("Číslo vlaku musí být číslo")
                except SpeedError:
                    print("Rychlost vlaku musí být kladný nenulový číslo")
                except CapacityError:
                    print("Kapacita vlaku musí být kladné nenulový číslo")
                trainlist.append(t)
                try:
                    for x in i["stanice"]:
                        t.addstation(x["jmeno"],x["vzdalenost"])
                except DuplicateStationError:
                    print("Stanice nesmí mít stejný název")
    except json.JSONDecodeError:
        print("Špatný format souboru trains.json")
    except FormatError:
        print("Format vlaku je špatný")
        
    

running = True
trainlist = []
while running:
    options = ["Pridat vlak","Smazat vlak","Přidat zastavku vlaku","Smazat zastavku vlaku","Výpis vlaku","Spustit simulaci","Načíst ze souboru","Ukončit"]
    showoptions(options)
    choice = input("Vybírám si: ")
    match choice:
        case "Pridat vlak" | "1":
            t = addtrain()
            trainlist.append(t)
        case "Smazat vlak" | "2":
            deletetrain(trainlist)
        case "Přidat zastavku vlaku" | "3":
            if(len(trainlist) == 0):
                print("Žádny vlaky nebyly vytvořeny")
            else:
                station = addstation(trainlist)
        case "Smazat zastavku vlaku" | "4":
            removestation(trainlist)
        case "Vypis vlaku" | "5":
            if(len(trainlist) == 0):
                print("Žádny vlaky nebyly vytvořeny")
            else:
                for i in trainlist:
                    print(i)
        case "Spustit simulaci" | "6":
            if(len(trainlist) == 0):
                print("Žádny vlaky nebyly vytvořeny")
            else:
                asyncio.run(main(trainlist))
        case "Načíst ze souboru" | "7":
            load(trainlist)
        case "Ukončit" | "8":
            running = False
        case _:
            print("Špatná volba")
    print("")
