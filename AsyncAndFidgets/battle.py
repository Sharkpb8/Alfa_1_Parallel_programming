from Wizard import *
from Enemy import *
import asyncio
import datetime
import random

def gettime():
    return f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

def attackmesage(attacker,atacked):
    return f"{gettime()}: {attacker.name} zautocil na {atacked.name}\n"

async def attackplayer(wizard,enemy,f):
    while(enemy.current_health > 0 and wizard.current_health > 0):
        await enemy.takedemage(await wizard.Fireball())
        f.write(attackmesage(wizard,enemy))
        print(enemy)

async def attackenemy(wizard,enemy,f):
    while(wizard.current_health > 0 and enemy.current_health > 0):
        await wizard.takedemage(await enemy.attack())
        f.write(attackmesage(enemy,wizard))
        print(wizard)

async def battle(wizard,enemy):
    f = open("log.txt","a")
    f.write(f"{gettime()}: souboj zacal mezi {wizard.name} a {enemy.name}\n")
    await asyncio.gather(attackenemy(wizard,enemy,f),attackplayer(wizard,enemy,f))
    if(wizard.current_health <=0 and enemy.current_health >0):
        print(f"Nepritel {enemy.name} vyral")
        f.write(f"{gettime()}: souboj vyhral nepritel {enemy.name}\n")
    elif(enemy.current_health <=0 and wizard.current_health >0):
        print(f"Hrac {wizard.name} vyhral")
        wizard.addxp(enemy.xpgained)
        f.write(f"{gettime()}: hrac {wizard.name} ziskal {enemy.xpgained}xp\n")
        f.write(f"{gettime()}: souboj vyhrrl hrac {wizard.name}\n")
    elif(enemy.current_health <=0 and wizard.current_health <=0):
        print(f"remiza hrac {wizard.name} a nepritel {enemy.name} zemreli")
        f.write(f"{gettime()}: remiza mezi hracem {wizard.name} a nepritelem {enemy.name}\n")
    f.close()

async def main(w):
    e = Enemy("lupic",random.randint(70,110),random.randint(5,15))
    await asyncio.gather(battle(w,e))