import serial
import discord
import asyncio

TOKEN = "NjYxOTI5MDQ4MzAxMjQwMzMz.Xg9kzw._EtntJCVaD35str2iS8nSPpYxgs"
ser = serial.Serial('/dev/ttyACM1', 9600,timeout = 10)
output = "Ready"
class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def my_background_task(self):
        await self.wait_until_ready()
        channel = self.get_channel(661989449214984192) # channel ID goes here
        while not self.is_closed():
            cc = ser.readline().decode()
            print(cc)
            if cc:
                output = cc
            #await channel.send(cc)
            await client.change_presence(status=discord.Status.online,activity=discord.Game(output))
            await asyncio.sleep(5)


client = MyClient()
client.run(TOKEN)
