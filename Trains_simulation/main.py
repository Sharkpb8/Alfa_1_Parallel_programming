from Train import *
from Error import *
from simulation import *
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
    with open("./Trains_simulation/trains.json","r",encoding="utf-8") as j:
        list = json.load(j)
        for i in list:
            t = Train(i["typ_vlaku"],i["cislo_vlaku"],LinkedList())
            trainlist.append(t)
            for x in i["stanice"]:
                t.addstation(x)
        
    

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
                Start(trainlist)
        case "Načíst ze souboru" | "7":
            load(trainlist)
        case "Ukončit" | "8":
            running = False
        case _:
            print("Špatná volba")
    print("")
