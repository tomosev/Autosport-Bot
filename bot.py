import discord
from discord.ext import commands
# files
from data import webCollectData
from embeds import EmbedWithFields
from images import driver_images, constructor_images
# env
from dotenv import load_dotenv
# packages
import os
import datetime

bot = discord.Client()
bot = commands.Bot(command_prefix="!")
# embed re-used fields
bot_name = "Motorsport Bot"
flagemoji = ":checkered_flag:"
caremoji = ":race_car:"
nl = '\n'
embed = discord.Embed()


@bot.event
async def on_ready():
    print('Green flag: {0.user}'.format(bot))


# Formula one commands


@bot.command(name="f1calandar")
# gets all races for a season
async def calandar(ctx):
    fields = []
    year = datetime.datetime.now().year
    data = webCollectData().apiRaceSchedule()
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
            f"Date: {date}{nl}Time: {time} (zulutime) {nl}Location: {circuit}  [{name} on Wikipedia]({url})"
        ])
    embed = EmbedWithFields(
        title=f"Formula 1 Race Calandar {year}",
        color=0xe60000,
        description=f"The current {year} Formula 1 calandar",
        fields=fields,
    )
    embed.set_footer(text=bot_name)
    await ctx.send(embed=embed)

# race results last race
# http://ergast.com/api/f1/current/last/results

# season results
# http://ergast.com/api/f1/2008/results/1


@bot.command(name="f1drivers")
# gets all formulaone drivers
async def drivers(ctx):
    fields = []
    year = datetime.datetime.now().year
    data = webCollectData().apiDriversAll(year)
    for race in data["MRData"]["DriverTable"]["Drivers"]:
        first_name = race["givenName"]
        last_name = race["familyName"]
        number = race["permanentNumber"]
        code = race["code"]
        fields.append([
            f"{caremoji}**{first_name} {last_name}**",
            f"Number: {number}{nl}Code: {code}"
        ])
    embed = EmbedWithFields(
        title=f"Formula 1 Driver List {year}",
        color=0xe60000,
        description=f"The current {year} Formula 1 driver list",
        fields=fields,
    )
    embed.set_footer(text=bot_name)
    await ctx.send(embed=embed)


@bot.command(name="f1driver")
# gets specific driver information
async def driver(ctx, arg):
    data = webCollectData().apiDriverInfo(name=arg)
    for race in data["MRData"]["DriverTable"]["Drivers"]:
        first_name = race["givenName"]
        last_name = race["familyName"]
        number = race["permanentNumber"]
        code = race["code"]
        unformated_dob = race["dateOfBirth"]
        nation = race["nationality"]
        url = race["url"]
        dateofbirth = datetime.datetime.strptime(
            unformated_dob, "%Y-%m-%d").strftime("%d/%m/%Y")
        embed = discord.Embed(title=f"{caremoji}{first_name} {last_name}",
                              description=f"**Number:** {number}{nl}**Code:** {code}{nl}**DOB**: {dateofbirth}{nl}**Nationality:** {nation}{nl}  [{first_name} {last_name} on Wikipedia]({url})", color=0xe60000)
        image = last_name.lower()
        if image in driver_images:
            embed.set_thumbnail(url=driver_images[image])
        embed.set_footer(text=bot_name)
        await ctx.send(embed=embed)


@bot.command(name="f1teams")
# gets all formula one constructors
async def constructors(ctx):
    fields = []
    year = datetime.datetime.now().year
    data = webCollectData().apiConstructorAll(year)
    for team in data["MRData"]["ConstructorTable"]["Constructors"]:
        name = team["name"]
        nation = team["nationality"]
        url = team["url"]
        fields.append([
            f"{caremoji}**{name}**",
            f"Origin: {nation}{nl}[More info]({url})"
        ])
    embed = EmbedWithFields(
        title=f"Formula 1 Team List {year}",
        color=0xe60000,
        description=f"The current {year} Formula 1 team list",
        fields=fields,
    )
    embed.set_footer(text=bot_name)
    await ctx.send(embed=embed)


@ bot.command(name="f1team")
# gets specific constructor information
async def constructor(ctx, arg):
    data = webCollectData().apiConstructorInfo(name=arg)
    for team in data["MRData"]["ConstructorTable"]["Constructors"]:
        name = team["name"]
        nation = team["nationality"]
        url = team["url"]
        embed = discord.Embed(title=f"{flagemoji}{name}",
                              description=f"**Origin:** {nation}{nl} [{name} on Wikipedia]({url})")
        image = name.lower()
        if image in constructor_images:
            embed.set_thumbnail(url=constructor_images[image])
        embed.set_footer(text=bot_name)
        await ctx.send(embed=embed)

load_dotenv()
KEY = os.environ.get("DISCORD_KEY")
bot.run(KEY)
