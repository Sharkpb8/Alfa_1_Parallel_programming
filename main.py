playerclasses = ["wizard"]

playerclass = None
while not playerclass:
    count =1
    print("Vyberte si svojí hráčskou classu")
    for i in playerclasses:
        print(f"{count}. {i}")

    playerchoice = input("Vybírám si: ")
    if(isinstance(int(playerchoice),int) and int(playerchoice) <= len(playerclasses)):
        playerclass = playerclasses[int(playerchoice)-1]
    elif(playerchoice in playerclasses):
        playerclass = playerchoice
        
