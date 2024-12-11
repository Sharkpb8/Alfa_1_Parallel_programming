playerclasses = ["wizard"]

classchoosen = False

while not classchoosen:
    count =1
    print("Vyberte si svojí hráčskou classu")
    for i in playerclasses:
        print(f"{count}. {i}")

    playerchoice = input("Vybírám si: ")