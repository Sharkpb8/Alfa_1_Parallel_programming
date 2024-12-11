from Wizard import *
from Enemy import *
import asyncio

async def attackplayer(wizard,enemy):
    while(enemy.current_health > 0 and wizard.current_health > 0):
        await enemy.takedemage(await wizard.Fireball())
        print(enemy.current_hp())

async def attackenemy(wizard,enemy):
    while(wizard.current_health > 0 and enemy.current_health > 0):
        await wizard.takedemage(await enemy.attack())
        print(wizard.current_hp())

async def battle(wizard,enemy):
    await asyncio.gather(attackenemy(wizard,enemy),attackplayer(wizard,enemy))
    if(wizard.current_health <=0):
        print("enemy vyral")
    elif(enemy.current_health <=0):
        print("hrac vyhral")

async def main():
    w = Wizard("nekdo")
    e = Enemy("lupič",100,10)
    await asyncio.gather(battle(w,e))

asyncio.run(main())