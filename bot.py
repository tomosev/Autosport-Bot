import discord
from discord.ext import commands
from data import webCollectData
from dotenv import load_dotenv
import os
import datetime
bot = discord.Client()
bot = commands.Bot(command_prefix="!")


@bot.command()
async def schedule(ctx):
    string = ""
    nl = '\n'
    time = datetime.datetime.now().year
    data = webCollectData().apiRaceSchedule()
    for race in data["MRData"]["RaceTable"]["Races"]:
        name = race["raceName"]
        circuit = race["Circuit"]["circuitName"]
        string += f"**{name}**: {circuit} {nl}{nl}"
    embed = discord.Embed(title=f"Race Schedule {time}",
                          description=string, color=0xe60000)
    await ctx.send(embed=embed)


@ bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


load_dotenv()
KEY = os.environ.get("DISCORD_KEY")
bot.run(KEY)
