import discord
from discord.ext import commands
# files
from data import webCollectData
from embeds import EmbedWithFields
# env
from dotenv import load_dotenv
# packages
import os
import datetime

bot = discord.Client()
bot = commands.Bot(command_prefix="!")
bot_name = "Motorsport Bot"


@bot.event
async def on_ready():
    print('Green flag: {0.user}'.format(bot))


@bot.command()
async def schedule(ctx):
    fields = []
    nl = '\n'
    time = datetime.datetime.now().year
    data = webCollectData().apiRaceSchedule()
    flagemoji = ":checkered_flag:"
    for race in data["MRData"]["RaceTable"]["Races"]:
        name = race["raceName"]
        circuit = race["Circuit"]["circuitName"]
        url = race["url"]
        unformatteddate = race["date"]
        unformattedtime = race["time"]
        time = unformattedtime[0:5]
        date = datetime.datetime.strptime(
            unformatteddate, "%Y-%m-%d").strftime("%d/%m/%Y")
        fields.append([
            f"{flagemoji}**{name}**",
            f"Date: {date} {nl} Time: {time}(zulutime) {nl} Location: {circuit}"
        ])
    embed = EmbedWithFields(
        title=f"Race Schedule {time}",
        color=0xe60000,
        description="",
        fields=fields,

    )
    embed.set_footer(text=bot_name)
    await ctx.send(embed=embed)


load_dotenv()
KEY = os.environ.get("DISCORD_KEY")
bot.run(KEY)
