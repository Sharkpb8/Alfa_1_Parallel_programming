import json
import asyncio

async def sendtrain(t):
    print("asdasd")

async def main(trainlist):
    await asyncio.gather(*(sendtrain(t) for t in trainlist))

