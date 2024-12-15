import json
import asyncio
import random

def openjson():
    with open("./Trains_simulation/config.json","r") as j:
        config = json.load(j)
        simulation = config["simulation"]
        return {"delay-chance":simulation['delay-chance'],"mimimum-delay":simulation['mimimum-delay'],"maximum-delay":simulation['maximum-delay']}
         

async def sendtrain(t):
    for i in t.getallstations():
        road = t.movetrain()
        config = openjson()
        print(f"vlak {t.type} {t.train_number} odjel z {road['from']}")
        await asyncio.sleep(1)
        if(random.randint(1,100)<=config["delay-chance"]):
            print("vlak ma spozdeni")
            print(f"{config['mimimum-delay']}, {config['maximum-delay']}")
            delay = round(random.uniform(config['mimimum-delay'], config['maximum-delay']), 2)
            print(delay)
            await asyncio.sleep(delay)
        print(f"vlak {t.type} {t.train_number} přijel do - {road['to']}")

async def main(trainlist):
    await asyncio.gather(*(sendtrain(t) for t in trainlist))

