from Wizard import *
from Enemy import *
import asyncio
import datetime

def gettime():
    return f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

async def attackplayer(wizard,enemy,f):
    while(enemy.current_health > 0 and wizard.current_health > 0):
        await enemy.takedemage(await wizard.Fireball())
        f.write(f"{gettime()}: {wizard.name} zautocil na {enemy.name}\n")
        print(enemy)

async def attackenemy(wizard,enemy,f):
    while(wizard.current_health > 0 and enemy.current_health > 0):
        await wizard.takedemage(await enemy.attack())
        f.write(f"{gettime()}: {enemy.name} zautocil na {wizard.name}\n")
        print(wizard)

async def battle(wizard,enemy):
    f = open("log.txt","a")
    f.write(f"{gettime()}: souboj zacal mezi {wizard.name} a {enemy.name}\n")
    await asyncio.gather(attackenemy(wizard,enemy,f),attackplayer(wizard,enemy,f))
    if(wizard.current_health <=0):
        print(f"Nepritel {enemy.name} vyral")
        f.write(f"{gettime()}: souboj vyhral nepritel {enemy.name}\n")
    elif(enemy.current_health <=0):
        print(f"Hrac {wizard.name} vyhral")
        wizard.addxp(enemy.xpgained)
        f.write(f"{gettime()}: hrac {wizard.name} ziskal {enemy.xpgained}xp\n")
        f.write(f"{gettime()}: souboj vyhrrl hrac {wizard.name}\n")
    f.close()

async def main(w):
    e = Enemy("lupic",90,10)
    await asyncio.gather(battle(w,e))