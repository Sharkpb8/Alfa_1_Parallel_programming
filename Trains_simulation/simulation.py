import json
import asyncio
import random

def openjson():
    with open("./Trains_simulation/config.json","r") as j:
        config = json.load(j)
        simulation = config["simulation"]
        return simulation
         

async def sendtrain(t):
    for i in range(t.gettrackssize()*2-2):
        road = t.movetrain()
        config = openjson()
        print(f"vlak {t.type} {t.train_number} odjel z - {road['from']}")
        t.consumefuel(road["distance"])
        traveltime = road["distance"]/t.speed
        await asyncio.sleep(traveltime)
        if(random.randint(1,100)<=config["delay-chance"]):
            print("vlak ma spozdeni")
            delay = round(random.uniform(config['mimimum-delay'], config['maximum-delay']), 2)
            print(delay)
            await asyncio.sleep(delay)
        print(f"vlak {t.type} {t.train_number} přijel do - {road['to']}")
        await t.removepassanger(road['to'],config)
        if(road["finish"]):
            t.current_fuel = t.fuel
            print("konec")
            break
        needsrefuel = t.needrefill(t.distancetonext())
        if(not needsrefuel):
            print("vlak netankuje - ",t.getcurrentfuel())
            await asyncio.gather(loadpassangers(t,config))
        else:
            await asyncio.gather(loadpassangers(t,config),refuel(t,config))

async def loadpassangers(t,config):
    fill = random.randint(config["min-fill"],config["max-fill"])/100
    passangers_bording = round(t.capacity*fill+1)
    for i in range(passangers_bording):
        result = t.addpassangers(await generatepassanger(t))
        if(result):
            print("Vlak je plný")
            break
        await asyncio.sleep(config["geton-time"])
    print("Do vlaku nastoupilo",passangers_bording)

async def refuel(t,config):
    print("valk tankuje -",t.getcurrentfuel())
    print("vlak potrebuje",t.fuelneeded())
    await asyncio.sleep(config["fuel-time"])
    new_fuel = round(t.fuelneeded()*(1+random.randint(0,config["max-refuel"]+1)/100))
    t.refuel(new_fuel)
    print("vlak tet má -",t.getcurrentfuel())

async def generatepassanger(t):
    stations = t.getallstations()
    followingstations = t.trainposition()
    if(not followingstations["direction"]):
        stations.remove(followingstations["current_station"])
        destination = random.choice(stations)
        return destination
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
        return destination

async def main(trainlist):
    print("Simulace začala")
    await asyncio.gather(*(sendtrain(t) for t in trainlist))
    print("Simulace skončila")

