from Train import *
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
    while not optionpicked:
        print("Vyber si typ")
        showoptions(allowedtypes)
        choice = input("Vybírám si: ")
    

running = True
trainlist = []
while running:
    options = ["Pridat vlak","Ukončit"]
    showoptions(options)
    choice = input("Vybírám si: ")
    match choice:
        case "Pridat vlak" | "1":
            addtrain()
        case "Ukončit" | "2":
            running = False
        case _:
            print("Špatná volba")
