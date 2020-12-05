import discord
from discord.ext import commands
# files
from data import formula1data
from embeds import EmbedWithFields
from images import driver_images, constructor_images, constructor_icons
# env
from dotenv import load_dotenv
# packages
import os
import datetime

bot = discord.Client()
bot = commands.Bot(command_prefix="!")
# embed re-used fields
bot_name = "Motorsport Bot"
f1logo = "<:F1logo:784857003225776128>"
caremoji = ":race_car:"
nl = '\n'
embed = discord.Embed()


@bot.event
async def on_ready():
    print('Green flag: {0.user}'.format(bot))


# Formula one commands

@bot.command(name="f1standings")
async def driverstandings(ctx):
    fields = []
    year = datetime.datetime.now().year
    data = formula1data().apiDriverStandings()
    for race in data["MRData"]["StandingsTable"]["StandingsLists"][0]["DriverStandings"]:
        postion = race["position"]
        points = race["points"]
        wins = race["wins"]
        driver_code = race["Driver"]["code"]
        driver_first = race["Driver"]["givenName"]
        driver_last = race["Driver"]["familyName"]
        team = race["Constructors"][0]["name"]
        teamname = team.lower()
        icon = ""
        if teamname in constructor_icons:
            icon = constructor_icons[teamname]
        fields.append([
            f"{icon} **{postion}**: {driver_code}",
            f"{driver_first} {driver_last}{nl}Points: {points}{nl}Wins: {wins}"
        ])
    embed = EmbedWithFields(
        title=f"Formula 1 {year} standings",
        color=0xe60000,
        description=f"The current standings for the {year} season",
        fields=fields,
    )
    embed.set_footer(text=bot_name)
    await ctx.send(embed=embed)


@bot.command(name="f1calandar")
# gets all races for a season
async def calandar(ctx):
    fields = []
    year = datetime.datetime.now().year
    data = formula1data().apiRaceSchedule()
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
            f"{f1logo} **{name}**",
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


@bot.command(name="f1latestresults")
# race results last race
async def lastresults(ctx):
    fields = []
    data = formula1data().apiLatestResults()
    race_name = data["MRData"]["RaceTable"]["Races"][0]["raceName"]
    for results in data["MRData"]["RaceTable"]["Races"][0]["Results"]:
        # race info
        # Driver results
        position = results["position"]
        driver_code = results["Driver"]["code"]
        status = results["status"]
        team = results["Constructor"]["name"]
        teamname = team.lower()
        icon = ""
        if teamname in constructor_icons:
            icon = constructor_icons[teamname]
        fields.append([
            f"{icon}**{position}**: {driver_code}",
            f"{status}"
        ])
    embed = EmbedWithFields(
        title=f"{f1logo} Results {race_name}",
        color=0xe60000,
        description=f"Results for the most recent {race_name}",
        fields=fields
    )
    embed.set_footer(text=bot_name)
    await ctx.send(embed=embed)


@bot.command(name="f1qualifying")
# quali results
async def latestqualifying(ctx):
    fields = []
    data = formula1data().apiLatestQuali()
    race_name = data["MRData"]["RaceTable"]["Races"][0]["raceName"]
    for results in data["MRData"]["RaceTable"]["Races"][0]["QualifyingResults"]:
        position = results["position"]
        driver_code = results["Driver"]["code"]
        Q1 = ""
        Q2 = ""
        Q3 = ""
        if Q1 in results["Q1"]:
            Q1 = results["Q1"]

        # if Q2 in results["Q2"]:
        #     Q2 = results["Q2"]

        # if Q3 in results["Q3"]:
        #     Q3 = results["Q3"]

        fields.append([
            f"{caremoji}**{position}**: {driver_code}",
            f"Q1: {Q1}{nl}Q2: {Q2}{nl}Q3: {Q3}"
        ])
    embed = EmbedWithFields(
        title=f"{f1logo}Qualifying Results {race_name}",
        color=0xe60000,
        description=f"Qualifying results for the most recent {race_name}",
        fields=fields
    )
    embed.set_footer(text=bot_name)
    await ctx.send(embed=embed)


@bot.command(name="f1drivers")
# gets all formulaone drivers
async def drivers(ctx):
    fields = []
    year = datetime.datetime.now().year
    data = formula1data().apiDriversAll(year)
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
    data = formula1data().apiDriverInfo(name=arg)
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
                              description=f"**Number:** {number}{nl}**Code:** {code}{nl}**DOB**: {dateofbirth}{nl}**Nationality:** {nation}{nl}  [{first_name} {last_name} on Wikipedia]({url})",
                              color=0xe60000)
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
    data = formula1data().apiConstructorAll(year)
    for team in data["MRData"]["ConstructorTable"]["Constructors"]:
        name = team["name"]
        nation = team["nationality"]
        url = team["url"]
        name_lower = name.lower()
        icon = ""
        if name_lower in constructor_icons:
            icon = constructor_icons[name_lower]
        fields.append([
            f"{icon} **{name}**",
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
    data = formula1data().apiConstructorInfo(name=arg)
    for team in data["MRData"]["ConstructorTable"]["Constructors"]:
        name = team["name"]
        nation = team["nationality"]
        url = team["url"]
        name_lower = name.lower()
        if name_lower in constructor_icons:
            icon = constructor_icons[name_lower]
        embed = discord.Embed(title=f"{icon} {name}",
                              description=f"**Origin:** {nation}{nl} [{name} on Wikipedia]({url})",
                              color=0xe60000)
        if name_lower in constructor_images:
            embed.set_thumbnail(url=constructor_images[name_lower])
        embed.set_footer(text=bot_name)
        await ctx.send(embed=embed)

load_dotenv()
KEY = os.environ.get("DISCORD_KEY")
bot.run(KEY)
