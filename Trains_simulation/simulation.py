import json
import asyncio
import random
import datetime
import os

def openjson():
    with open("./Trains_simulation/config.json","r") as j:
        config = json.load(j)
        simulation = config["simulation"]
        return simulation

async def log(text,t):
    if(os.path.isdir("./Trains_simulation/logs") == False):
        os.mkdir("./Trains_simulation/logs")
    with open(f"./Trains_simulation/logs/{t.concat()}.txt", "a",encoding="utf-8") as log_file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{timestamp}]: {text}\n")        

async def sendtrain(t):
    await log("Simulace začala",t)
    for i in range(t.gettrackssize()*2-2):
        road = t.movetrain()
        config = openjson()
        await log(f"vlak {t.type} {t.train_number} odjel z - {road['from']}",t)
        t.consumefuel(road["distance"])
        traveltime = road["distance"]/t.speed
        await asyncio.sleep(traveltime)
        if(random.randint(1,100)<=config["delay-chance"]):
            delay = round(random.uniform(config['mimimum-delay'], config['maximum-delay']), 2)
            await log(f"Vlak ma spoždění: {delay}s",t)
            await asyncio.sleep(delay)
        await log(f"vlak {t.type} {t.train_number} přijel do - {road['to']}",t)
        await t.removepassanger(road['to'],config,log,t)
        if(road["finish"]):
            t.current_fuel = t.fuel
            break
        needsrefuel = t.needrefill(t.distancetonext())
        if(not needsrefuel):
            await log(f"vlak netankuje a má {t.getcurrentfuel()}L paliva",t)
            await asyncio.gather(loadpassangers(t,config))
        else:
            await asyncio.gather(loadpassangers(t,config),refuel(t,config))
    await log("Simulace skončila\n",t)

async def loadpassangers(t,config):
    fill = random.randint(config["min-fill"],config["max-fill"])/100
    passangers_bording = round(t.capacity*fill+1)
    for i in range(passangers_bording):
        result = t.addpassangers(await generatepassanger(t))
        if(result):
            await log("Vlak je celý zaplněný cestujícíma a další už nemužou nastoupit",t)
            break
        await asyncio.sleep(config["geton-time"])
    await log(f"Do vlaku nastoupilo: {passangers_bording} cestujících",t)

async def refuel(t,config):
    await log(f"Valk tankuje protože má {t.getcurrentfuel()}L a na cestu potřebuje ještě {t.fuelneeded()}L",t)
    await asyncio.sleep(config["fuel-time"])
    new_fuel = round(t.fuelneeded()*(1+random.randint(0,config["max-refuel"]+1)/100))
    t.refuel(new_fuel)
    await log(f"Vlak má po natankování {t.getcurrentfuel()}",t)

async def generatepassanger(t):
    stations = t.getallstations()
    followingstations = t.trainposition()
    if(not followingstations["direction"]):
        stations.remove(followingstations["current_station"])
        destination = random.choice(stations)
        return destination
    else:
        index = stations.index(followingstations["current_station"])
        if(index == 0):
            return None
        avaiablestatiosn = []
        for i in range(index):
            avaiablestatiosn.append(stations[i])
        destination = random.choice(list(avaiablestatiosn))
        return destination

async def main(trainlist):
    print("Simulace začala")
    await asyncio.gather(*(sendtrain(t) for t in trainlist))
    print("Simulace skončila")

