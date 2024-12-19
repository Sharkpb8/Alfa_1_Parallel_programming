from Train import *
from simulation import *
import json
import asyncio
import ast

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

def convert_input(value):
    try:
        return ast.literal_eval(value)
    except (ValueError, SyntaxError):
        return value

def addtrain():
    newtrain = {"type":None,"train_number":None,"speed":None,"capacity":None,"fuel":None,"consumption":None}
    while True:
        newtrain["type"] = convert_input(input("Vyber typ valku: "))
        newtrain["train_number"] = convert_input(input("Vyber číslo vlaku: "))
        newtrain["speed"] = convert_input(input("Vyber rychlost vlaku (km/s): "))
        newtrain["capacity"] = convert_input(input("Vyber kapacitu valku: "))
        newtrain["fuel"] = convert_input(input("Vyber maximálni nádrž vlaku: "))
        newtrain["consumption"] = convert_input(input("Vyber spotřebu vlaku (L/km): "))
        try:
            t = Train(newtrain["type"],newtrain["train_number"],newtrain["speed"],newtrain["capacity"],newtrain["fuel"],newtrain["consumption"],LinkedList())
        except TypeTypeError:
            print("Chyba: Typ vlaku musí být řetězec.")
        except TrainTypeError:
            print(f"Chyba: Typ vlaku '{newtrain['type']}' není povolen.")
        except TrainNumberTypeError:
            print("Chyba: Číslo vlaku musí být celé číslo.")
        except TrainNumberLenghtError:
            print("Chyba: Číslo vlaku musí mít 4 číslice.")
        except TracksTypeError:
            print("Chyba: Koleje musí být instance třídy LinkedList.")
        except SpeedTypeError:
            print("Chyba: Rychlost musí být celé číslo.")
        except SpeedError:
            print("Chyba: Rychlost musí být větší než nula.")
        except CapacityTypeError:
            print("Chyba: Kapacita musí být celé číslo.")
        except CapacityError:
            print("Chyba: Kapacita musí být větší než nula.")
        except FuelTypeError:
            print("Chyba: Palivo musí být celé číslo.")
        except FuelError:
            print("Chyba: Palivo musí být větší než nula.")
        except ConsumptionTypeError:
            print("Chyba: Spotřeba musí být celé číslo.")
        except ConsumptionError:
            print("Chyba: Spotřeba musí být větší než nula.")
        except json.JSONDecodeError:
            print("Chyba: Nelze přečíst nebo zpracovat 'config.json'.")
        except Exception as e:
            print(f"Neočekávaná chyba: {e}")
        else:
            return t


def addstation(trainlist):
    newstation = {"Name":None,"Distance":None}
    running = True
    runningstation = True
    while running:
        print("Pro který vlak chce přidat stanici ?")
        showotrainptions(trainlist)
        choice = input("Vybírám si: ")
        try:
            numberchoise = int(choice)
            t = trainlist[numberchoise-1]
            if(len(trainlist)<numberchoise):
                raise Exception
            else:
                while runningstation:
                    try:
                        newstation["Name"] = convert_input(input("Jmeno zastavky: "))
                        newstation["Distance"] = convert_input(input("Vzdálenost do zastávky (km): "))
                        t.addstation(newstation["Name"],newstation["Distance"])
                    except EmptyInputError:
                        print("Chyba: Chybí vstupní hodnoty (data nebo vzdálenost).")
                    except DataTypeError:
                        print("Chyba: Jméno zastávky musí být písmena.")
                    except DataLenghtError:
                        print("Chyba: Jméno zastávky musí být minimálně 3 znaky dlouhé.")
                    except DistanceTypeError:
                        print("Chyba: Vzdálenost musí být celé číslo.")
                    except DistanceLenghtError:
                        print("Chyba: Vzdálenost nemůže být záporná.")
                    except NextNodeError:
                        print("Chyba: Následující uzel není platný (musí být Node nebo None).")
                    except PrevNodeError:
                        print("Chyba: Předchozí uzel není platný (musí být Node nebo None).")
                    except Exception as e:
                        print(f"Neočekávaná chyba: {e}")
                    else:
                        running = False
                        break
        except ValueError:
            temptrainlist = []
            showotrainptions(trainlist)
            count = 0
            for i in temptrainlist:
                if(choice == i):
                    t = trainlist[count]
                    while runningstation:
                        try:
                            newstation["Name"] = convert_input(input("Jmeno zastavky: "))
                            newstation["Distance"] = convert_input(input("Vzdálenost do zastávky (km): "))
                            t.addstation(newstation["Name"],newstation["Distance"])
                        except EmptyInputError:
                            print("Chyba: Chybí vstupní hodnoty (data nebo vzdálenost).")
                        except DataTypeError:
                            print("Chyba: Jméno zastávky musí být písmena.")
                        except DataLenghtError:
                            print("Chyba: Jméno zastávky musí být minimálně 3 znaky dlouhé.")
                        except DistanceTypeError:
                            print("Chyba: Vzdálenost musí být celé číslo.")
                        except DistanceLenghtError:
                            print("Chyba: Vzdálenost nemůže být záporná.")
                        except NextNodeError:
                            print("Chyba: Následující uzel není platný (musí být Node nebo None).")
                        except PrevNodeError:
                            print("Chyba: Předchozí uzel není platný (musí být Node nebo None).")
                        except DuplicateStationError:
                            print("Chyba: Stanice nesmí mýt duplikátní jméno")
                        except Exception as e:
                            print(f"Neočekávaná chyba: {e}")
                        else:
                            running = False
                            break
                else:
                    count +=1
            print("Neplatný výběr vlaku")
        except Exception:
            print("Neplatný výběr vlaku")

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
        if(not optionpicked):
            print("Špatná volba")

def load(trainlist):
    try:
        with open("./Trains_simulation/trains.json","r",encoding="utf-8") as j:
            loadlist = json.load(j)
            if(len(loadlist) == 0):
                return print("V souboru trains.json se nic nenachází")
            for i in loadlist:
                try:
                    t = Train(i["typ_vlaku"],i["cislo_vlaku"],i["rychlost"],i["kapacita"],i["nadrz"],i["spotreba"],LinkedList())
                except TypeTypeError:
                    print("Chyba: Typ vlaku musí být řetězec.")
                except TrainTypeError:
                    print(f"Chyba: Typ vlaku '{i['type']}' není povolen.")
                except TrainNumberTypeError:
                    print("Chyba: Číslo vlaku musí být celé číslo.")
                except TrainNumberLenghtError:
                    print("Chyba: Číslo vlaku musí mít 4 číslice.")
                except TracksTypeError:
                    print("Chyba: Koleje musí být instance třídy LinkedList.")
                except SpeedTypeError:
                    print("Chyba: Rychlost musí být celé číslo.")
                except SpeedError:
                    print("Chyba: Rychlost musí být větší než nula.")
                except CapacityTypeError:
                    print("Chyba: Kapacita musí být celé číslo.")
                except CapacityError:
                    print("Chyba: Kapacita musí být větší než nula.")
                except FuelTypeError:
                    print("Chyba: Palivo musí být celé číslo.")
                except FuelError:
                    print("Chyba: Palivo musí být větší než nula.")
                except ConsumptionTypeError:
                    print("Chyba: Spotřeba musí být celé číslo.")
                except ConsumptionError:
                    print("Chyba: Spotřeba musí být větší než nula.")
                except json.JSONDecodeError:
                    print("Chyba: Nelze přečíst nebo zpracovat 'config.json'.")
                except Exception as e:
                    print(f"Neočekávaná chyba: {e}")
                trainlist.append(t)
                try:
                    for x in i["stanice"]:
                        t.addstation(x["jmeno"],x["vzdalenost"])
                except EmptyInputError:
                    print("Chyba: Chybí vstupní hodnoty (data nebo vzdálenost).")
                except DataTypeError:
                    print("Chyba: Jméno zastávky musí být písmena.")
                except DataLenghtError:
                    print("Chyba: Jméno zastávky musí být minimálně 3 znaky dlouhé.")
                except DistanceTypeError:
                    print("Chyba: Vzdálenost musí být celé číslo.")
                except DistanceLenghtError:
                    print("Chyba: Vzdálenost nemůže být záporná.")
                except NextNodeError:
                    print("Chyba: Následující uzel není platný (musí být Node nebo None).")
                except PrevNodeError:
                    print("Chyba: Předchozí uzel není platný (musí být Node nebo None).")
                except DuplicateStationError:
                    print("Chyba: Stanice nesmí mýt duplikátní jméno")
                except Exception as e:
                    print(f"Neočekávaná chyba: {e}")
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
