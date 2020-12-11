import discord
from discord.ext import commands

from data import formula1data
from embeds import EmbedWithFields, f1logo, nl, bot_name
from images import driver_images, constructor_images, constructor_icons

import datetime
year = datetime.datetime.now().year


class formulaOneCommands(commands.Cog):
    @commands.command(name="f1driverstandings")
    async def driverstandings(self, ctx):
        fields = []
        data = formula1data().apiDriverStandings()
        for race in data["MRData"]["StandingsTable"]["StandingsLists"][0][
            "DriverStandings"
        ]:
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
            fields.append(
                [
                    f"{icon} **{postion}**: {driver_code}",
                    f"{driver_first} {driver_last}{nl}Points: {points}{nl}Wins: {wins}",
                ]
            )
        embed = EmbedWithFields(
            title=f"Formula 1 {year} Driver Standings",
            color=0xDB1921,
            description=f"The current driver standings for the {year} season",
            fields=fields,
        )
        embed.set_footer(text=bot_name)
        await ctx.send(embed=embed)

    @commands.command(name="f1teamstandings")
    async def constructorstandings(self, ctx):
        fields = []
        data = formula1data().apiConstructorStandings()
        for results in data["MRData"]["StandingsTable"]["StandingsLists"][0][
            "ConstructorStandings"
        ]:
            position = results["position"]
            points = results["points"]
            wins = results["wins"]
            team = results["Constructor"]["name"]
            teamname = team.lower()
            icon = ""
            if teamname in constructor_icons:
                icon = constructor_icons[teamname]
            fields.append(
                [f"{icon} **{position}**: {team}",
                    f"Points: {points}{nl}Wins: {wins}"]
            )
        embed = EmbedWithFields(
            title=f"Formula 1 {year} Constructor Standings",
            color=0xDB1921,
            description=f"The current constructor standings for the {year} season",
            fields=fields,
        )
        embed.set_footer(text=bot_name)
        await ctx.send(embed=embed)

    @commands.command(name="f1calendar")
    # gets all races for a season
    async def calendar(self, ctx):
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
            date = datetime.datetime.strptime(unformatteddate, "%Y-%m-%d").strftime(
                "%d-%m-%Y"
            )
            fields.append(
                [
                    f"{f1logo} **{name}**",
                    f"Date: {date}{nl}Time: {time} (zulutime) {nl}Location: {circuit}  [{name} on Wikipedia]({url})",
                ]
            )
        embed = EmbedWithFields(
            title=f"Formula 1 Race Calandar {year}",
            color=0xDB1921,
            description=f"The current {year} Formula 1 calandar",
            fields=fields,
        )
        embed.set_footer(text=bot_name)
        await ctx.send(embed=embed)

    @commands.command(name="f1latestresults")
    # race results last race
    async def lastresults(self, ctx):
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
            fields.append(
                [f"{icon}** {position}**: {driver_code}", f"{status}"])
        embed = EmbedWithFields(
            title=f"{f1logo} Results {race_name}",
            color=0xDB1921,
            description=f"Results for the most recent {race_name}",
            fields=fields,
        )
        embed.set_footer(text=bot_name)
        await ctx.send(embed=embed)

    @commands.command(name="f1qualifying")
    # quali results
    async def latestqualifying(self, ctx):
        fields = []
        data = formula1data().apiLatestQuali()
        race_name = data["MRData"]["RaceTable"]["Races"][0]["raceName"]
        for results in data["MRData"]["RaceTable"]["Races"][0]["QualifyingResults"]:
            position = results["position"]
            driver_code = results["Driver"]["code"]
            teamname_unformatted = results["Constructor"]["name"]
            teamname = teamname_unformatted.lower()
            icon = ""
            if teamname in constructor_icons:
                icon = constructor_icons[teamname]
            Q1, Q2, Q3 = "", "", ""

            if "Q1" in results:
                Q1 = results["Q1"]
            else:
                Q1 = ""
            if "Q2" in results:
                Q2 = results["Q2"]
            else:
                Q2 = ""
            if "Q3" in results:
                Q3 = results["Q3"]
            else:
                Q3 = ""

            fields.append(
                [
                    f"{icon} **{position}**: {driver_code}",
                    f"Q1: {Q1}{nl}Q2: {Q2}{nl}Q3: {Q3}",
                ]
            )
        embed = EmbedWithFields(
            title=f"{f1logo} Qualifying Results {race_name}",
            color=0xDB1921,
            description=f"Qualifying results for the most recent {race_name}",
            fields=fields,
        )
        embed.set_footer(text=bot_name)
        await ctx.send(embed=embed)

    @commands.command(name="f1drivers")
    # gets all formulaone drivers
    async def drivers(self, ctx):
        fields = []
        year = datetime.datetime.now().year
        data = formula1data().apiDriversAll(year)
        for race in data["MRData"]["DriverTable"]["Drivers"]:
            first_name = race["givenName"]
            last_name = race["familyName"]
            number = race["permanentNumber"]
            code = race["code"]
            fields.append(
                [
                    f"{f1logo}** {first_name} {last_name}**",
                    f"Number: {number}{nl}Code: {code}",
                ]
            )
        embed = EmbedWithFields(
            title=f"Formula 1 Driver List {year}",
            color=0xDB1921,
            description=f"The current {year} Formula 1 driver list",
            fields=fields,
        )
        embed.set_footer(text=bot_name)
        await ctx.send(embed=embed)

    @commands.command(name="f1driver")
    # gets specific driver information
    async def driver(self, ctx, arg):
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
                unformated_dob, "%Y-%m-%d"
            ).strftime("%d-%m-%Y")
            embed = discord.Embed(
                title=f"{f1logo} {first_name} {last_name}",
                description=f"**Number:** {number}{nl}**Code:** {code}{nl}**DOB**: {dateofbirth}{nl}**Nationality:** {nation}{nl}  [{first_name} {last_name} on Wikipedia]({url})",
                color=0xDB1921,
            )
            image = last_name.lower()
            if image in driver_images:
                embed.set_thumbnail(url=driver_images[image])
            embed.set_footer(text=bot_name)
            await ctx.send(embed=embed)

    @commands.command(name="f1teams")
    # gets all formula one constructors
    async def constructors(self, ctx):
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
            fields.append(
                [f"{icon} **{name}**",
                    f"Origin: {nation}{nl}[More info]({url})"]
            )
        embed = EmbedWithFields(
            title=f"Formula 1 Team List {year}",
            color=0xDB1921,
            description=f"The current {year} Formula 1 team list",
            fields=fields,
        )
        embed.set_footer(text=bot_name)
        await ctx.send(embed=embed)

    @commands.command(name="f1team")
    # gets specific constructor information
    async def constructor(self, ctx, arg):
        data = formula1data().apiConstructorInfo(name=arg)
        for team in data["MRData"]["ConstructorTable"]["Constructors"]:
            name = team["name"]
            nation = team["nationality"]
            url = team["url"]
            name_lower = name.lower()
            if name_lower in constructor_icons:
                icon = constructor_icons[name_lower]
            embed = discord.Embed(
                title=f"{icon} {name}",
                description=f"**Origin:** {nation}{nl} [{name} on Wikipedia]({url})",
                color=0xDB1921,
            )
            if name_lower in constructor_images:
                embed.set_thumbnail(url=constructor_images[name_lower])
            embed.set_footer(text=bot_name)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(formulaOneCommands(commands))
