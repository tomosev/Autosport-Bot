import discord
from data import webCollectData
from dotenv import load_dotenv
import os
import json

load_dotenv()

KEY = os.environ.get("DISCORD_KEY")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# class myclient(discord.Client): 
#     async def on_ready(self):
#         data = webCollectData().apiRoundData()
#         print(data['MRData'] ['RaceTable'] ['season']) 


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!race schedule'):
        data = webCollectData().apiRaceSchedule()
        for race in data["MRData"] ["RaceTable"] ["Races"]:
            name = race["raceName"]
            circuit = race["Circuit"] ["circuitName"]
            messagecontent = name, circuit
            await message.channel.send(messagecontent)

        



client.run(KEY)

