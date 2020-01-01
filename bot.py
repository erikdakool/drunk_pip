import serial
import discord
import asyncio

ser = serial.Serial('/dev/ttyACM17', 9600)
TOKEN = "NjYxOTI5MDQ4MzAxMjQwMzMz.XgzepQ.0nhBid37D0WxrWZMef5UJhVKRUg"

import asyncio
client = discord.Client()
async def my_background_task():
    await client.wait_until_ready()
    counter = 0
    channel = discord.Object(id='661989449214984192')
    while not client.is_closed:
        counter += 1
        print(counter)
        await client.send_message(channel, counter)
        await asyncio.sleep(5)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.loop.create_task(my_background_task())
client.run(TOKEN)

while True:
    cc=str(ser.readline())
    print(cc)