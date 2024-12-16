import json
import asyncio
import random

def openjson():
    with open("./Trains_simulation/config.json","r") as j:
        config = json.load(j)
        simulation = config["simulation"]
        return {"delay-chance":simulation['delay-chance'],"mimimum-delay":simulation['mimimum-delay'],"maximum-delay":simulation['maximum-delay']}
         

async def sendtrain(t):
    for i in range(t.gettrackssize()*2-2):
        road = t.movetrain()
        config = openjson()
        print(f"vlak {t.type} {t.train_number} odjel z - {road['from']}")
        traveltime = road["distance"]/t.speed
        await asyncio.sleep(traveltime)
        if(random.randint(1,100)<=config["delay-chance"]):
            print("vlak ma spozdeni")
            delay = round(random.uniform(config['mimimum-delay'], config['maximum-delay']), 2)
            print(delay)
            await asyncio.sleep(delay)
        print(f"vlak {t.type} {t.train_number} přijel do - {road['to']}")
        await asyncio.gather(loadpassangers(t))

async def loadpassangers(t):
    stations = t.getallstations()
    followingstations = t.trainposition()
    if(not followingstations["direction"]):
        stations.remove(followingstations["current_station"])
        destination = random.choice(stations)
        print(destination)
    else:
        # print("stanice aktualni ",followingstations["current_station"])
        index = stations.index(followingstations["current_station"])
        if(index == 0):
            return None
        # print("index",str(index))
        avaiablestatiosn = []
        for i in range(index):
            avaiablestatiosn.append(stations[i])
            # print("pridano",str(stations[i]))
        destination = random.choice(list(avaiablestatiosn))
        print(destination)
    t.addpassangers(1)

async def main(trainlist):
    await asyncio.gather(*(sendtrain(t) for t in trainlist))

