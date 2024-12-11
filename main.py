from battle import *
from Wizard import *

def Chooseclass():
    classes = ["wizard","warrior","cleric","druid"]
    playerclass = None

    while not playerclass:
        count =1
        print("Vyberte si svojí hráčskou classu")
        for i in classes:
            print(f"{count}. {i}")
            count +=1

        playerchoice = input("Vybírám si: ")
        if(playerchoice in classes):
            playerclass = playerchoice
        elif(playerchoice.isdigit()):
            if(int(playerchoice) <= len(classes)):
                playerclass = classes[int(playerchoice)-1]
        else:
            print("špatně zadaná hodnota")
    return playerclass

def createcharacter(playerclass,username):
    match playerclass:
        case "wizard":
            w = Wizard(username)
            return w 
        case "warrior":
            print()
        case "cleric":
            print()
        case "druid":
            print()

playerchoice = Chooseclass()
username = input("Zadejte jmeno postavy: ")
character = createcharacter(playerchoice,username)

asyncio.run(main(character))
