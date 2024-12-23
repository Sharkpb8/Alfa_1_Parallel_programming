from src.Train import *
from src.simulation import *
import json
import asyncio
import ast

def showoptions(list):
    """
    Displays the items in a list with numbered options.

    :param list: A list of items to display as options.
    :type list: list
    """
    count =1
    for i in list:
        print(f"{count}. {i}")
        count +=1

def showotrainptions(trainlist):
    """
    Displays the train options with their type and train number.

    :param trainlist: A list of Train objects to display as options.
    :type trainlist: list
    """
    count =1
    for i in trainlist:
        print(f"{count}. {trainlist[count-1].type}{trainlist[count-1].train_number}")
        count +=1

def convert_input(value):
    """
    Tries to convert a string input into a Python literal (e.g., int, float, list, etc.).
    If conversion fails, returns the original string.

    :param value: The input string to be evaluated.
    :type value: str
    :return: The converted value or the original string if conversion fails.
    :rtype: any
    """
    try:
        return ast.literal_eval(value)
    except (ValueError, SyntaxError):
        return value

def check_config():
    with open("./config.json","r") as j:
        config = json.load(j)
        if(not isinstance(config,dict)):
            raise ConfigDictionaryError
        if(not isinstance(config["allowedtypes"],list)):
            raise ConfigListError
        for i in config["allowedtypes"]:
            if(not isinstance(i,str)):
                raise ConfigTrainTypeError
        simulation = config["simulation"]
        for i in simulation.values():
            if(not isinstance(i,(int,float))):
                raise ConfigSimulationDataError
            if(isinstance(i,bool)):
                raise ConfigSimulationDataError
        

def addtrain():
    """
    Creates new train based on user input

    :returns: new train
    :rtype: train
    """
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
            print("Chyba: Typ vlaku musí být písmena.")
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

def picktrain(trainlist,prompt):
    """
    Prompts the user to select a train from a list, either by its position in the list (integer input)
    or by its unique identifier (string input). If the input is invalid, the user is prompted to try again.

    :param trainlist: A list of train objects to choose from.
    :type trainlist: list
    :param prompt: A message to display when prompting the user for input.
    :type prompt: str
    :return: The selected train object from the list.
    :rtype: object
    """
    while True:
        print(prompt)
        showotrainptions(trainlist)
        choice = input("Vybírám si: ")
        try:
            numberchoise = int(choice)
            if(len(trainlist)<numberchoise or numberchoise <= 0):
                raise ChoiceError
            t = trainlist[numberchoise-1]
            return t
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
                    return t
                else:
                    count +=1
            print("Špatná volba")
        except ChoiceError:
            print("Špatná volba")


def addstation(trainlist):
    """
    creates new station for specific train

    :param trainlist: list of trains from where to select  
    """
    newstation = {"Name":None,"Distance":None}
    running = True
    runningstation = True
    while running:
        t = picktrain(trainlist,"Pro který vlak chce přidat stanici ?")
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
                print("Chyba: Zastávka musí mít unikátní jméno pro tuto trať")
            except NotReachableStationError:
                print("Chyba: Tato stanice by nebylo mozna dosáhnout s tímto vlakem")
            except Exception as e:
                print(f"Neočekávaná chyba: {e}")
            else:
                running = False
                break

def deletetrain(trainlist):
    """
    Deletes train by choice

    :param trainlist: train list from where to delete train  
    """
    optionpicked = False
    while not optionpicked:
        print("Který vlak chcete smazat?")
        showotrainptions(trainlist)
        choice = input("Vybírám si: ")
        try:
            numberchoise = int(choice)
            if(len(trainlist)<numberchoise or numberchoise <= 0):
                raise ChoiceError
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
            print("Špatná volba")
        except ChoiceError:
            print("Špatná volba")
    

def removestation(trainlist):
    """
    Removes station from train

    :param trainlist: trainlist from where to delete train  
    """
    optionpicked = False
    t = picktrain(trainlist,"Pro který vlak chce smazat stanici ?")
    while not optionpicked:
            stations = t.getallstations()
            showoptions(stations)
            choice = input("Vybírám si: ")
            try:
                numberchoise = int(choice)
                if(len(t.getallstations())<numberchoise or numberchoise <= 0):
                    raise ChoiceError
                t.removestation(stations[numberchoise-1])
                break
            except ValueError:
                if(choice in stations):
                    t.removestation(choice)
                    break
            except ChoiceError:
                print("Špatná volba")


def load(trainlist):
    """
    load trains and stations from json
    :param trainlist: trainlist where to insert trains  
    """
    try:
        with open("./trains.json","r",encoding="utf-8") as j:
            loadlist = json.load(j)
            if(len(loadlist) == 0):
                return print("V souboru trains.json se nic nenachází")
            for i in loadlist:
                try:
                    t = Train(i["typ_vlaku"],i["cislo_vlaku"],i["rychlost"],i["kapacita"],i["nadrz"],i["spotreba"],LinkedList())
                except TypeTypeError:
                    print("Chyba: Typ vlaku musí být řetězec.")
                except TrainTypeError:
                    print(f"Chyba: Typ vlaku '{i['typ_vlaku']}' není povolen.")
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
                except KeyError as e:
                    print(f"Chyba: U vlaku chybý {e}")
                except Exception as e:
                    print(f"Neočekávaná chyba: {e}")
                else:
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
                    except KeyError as e:
                        print(f"Chyba: U stanice chybý {e}")
                    except Exception as e:
                        print(f"Neočekávaná chyba: {e}")
    except json.JSONDecodeError:
        print("Chyba: Špatný format souboru trains.json")
    except FileNotFoundError:
        print("Chyba: Složka trains.json nebyla vytvořena")
    except FormatError:
        print("Format vlaku je špatný")
        
    
def Run():
    """
    Main program loop
    :param 1: Add train to list
    :param 2: Deletes train from lsit
    :param 3: Adds station to train
    :param 4: Deletes station from train
    :param 5: Prints out all current trains
    :param 6: Starts simulation
    :param 7: Loads trains and station from json
    :param 8: ends program
    """
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
                    addstation(trainlist)
            case "Smazat zastavku vlaku" | "4":
                emptytrains = True
                for i in trainlist:
                    if (len(i.getallstations())>=1):
                        emptytrains = False
                if(emptytrains):
                    print("Všechny vlaky nemají stanice")
                else:
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
                    try:
                        check_config()
                    except json.JSONDecodeError:
                        print("Chyba: Nelze přečíst nebo zpracovat 'config.json'.")
                    except ConfigDictionaryError:
                        print("Chyba: Config musí být dictionary")
                    except ConfigListError:
                        print("Chyba: List povolených typů vlaků musí být list")
                    except ConfigSimulationDataError:
                        print("Chyba: Špatný datový typ pro hodnoty v simulaci")
                    except ConfigTrainTypeError:
                        print("Chyba: Povolený typ vlaku musí být písmena")
                    except FileNotFoundError:
                        print("Chyba: Soubor config.json nebyl vytvořen")
                    else:
                        asyncio.run(main(trainlist))
            case "Načíst ze souboru" | "7":
                load(trainlist)
            case "Ukončit" | "8":
                running = False
            case _:
                print("Špatná volba")
        print("")

if __name__ == "__main__":
    Run()