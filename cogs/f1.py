import discord
from discord.ext import commands
import config
import f1data
from embeds import EmbedWithFields

from images import driver_images, constructor_images, constructor_icons


class formulaOneCommands(commands.Cog):
    @commands.command(name="driverstandings")
    async def f1_driver_standings(self, ctx):
        fields = []
        data = f1data.f1_driver_standings()

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
            icon = ""

            if team.lower() in constructor_icons:
                icon = constructor_icons[team.lower()]

            fields.append(
                [
                    f"{icon} **{postion}**: {driver_code}",
                    f"{driver_first} {driver_last}{config.NL}Points: {points}{config.NL}Wins: {wins}",
                ]
            )

        embed = EmbedWithFields(
            title=f"Formula 1 {f1data.year} Driver Standings",
            color=0xDB1921,
            description=f"The current driver standings for the {f1data.year} season",
            fields=fields,
        )
        embed.set_footer(text=config.BOT_FOOTER)
        await ctx.send(embed=embed)

    @commands.command(name="teamstandings")
    async def f1_team_standings(self, ctx):
        fields = []
        data = f1data.f1_team_standings()

        for results in data["MRData"]["StandingsTable"]["StandingsLists"][0][
            "ConstructorStandings"
        ]:
            position = results["position"]
            points = results["points"]
            wins = results["wins"]
            team = results["Constructor"]["name"]
            icon = ""

            if team.lower() in constructor_icons:
                icon = constructor_icons[team.lower()]

            fields.append(
                [
                    f"{icon} **{position}**: {team}",
                    f"Points: {points}{config.NL}Wins: {wins}",
                ]
            )

        embed = EmbedWithFields(
            title=f"Formula 1 {f1data.year} Constructor Standings",
            color=0xDB1921,
            description=f"The current constructor standings for the {f1data.year} season",
            fields=fields,
        )
        embed.set_footer(text=config.BOT_FOOTER)
        await ctx.send(embed=embed)

    @commands.command(name="calendar")
    async def f1_calendar(self, ctx):
        fields = []
        data = f1data.f1_race_schedule()

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
                    f"{config.F1_LOGO} **{name}**",
                    f"Date: {date}{config.NL}Time: {time} (zulutime) {config.NL}Location: {circuit}  [{name} on Wikipedia]({url})",
                ]
            )

        embed = EmbedWithFields(
            title=f"Formula 1 Race Calandar {f1data.year}",
            color=0xDB1921,
            description=f"The current {f1data.year} Formula 1 calandar",
            fields=fields,
        )
        embed.set_footer(text=config.BOT_FOOTER)
        await ctx.send(embed=embed)

    @commands.command(name="latestresults")
    async def f1_last_results(self, ctx):
        fields = []
        data = f1data.f1_latest_results()

        for results in data["MRData"]["RaceTable"]["Races"][0]["Results"]:
            position = results["position"]
            driver_code = results["Driver"]["code"]
            status = results["status"]
            team = results["Constructor"]["name"]
            icon = ""

            if team.lower() in constructor_icons:
                icon = constructor_icons[team.lower()]

            fields.append([f"{icon}** {position}**: {driver_code}", f"{status}"])

        race_name = data["MRData"]["RaceTable"]["Races"][0]["raceName"]
        embed = EmbedWithFields(
            title=f"{config.F1_LOGO} Results {race_name}",
            color=0xDB1921,
            description=f"Results for the most recent {race_name}",
            fields=fields,
        )
        embed.set_footer(text=config.BOT_FOOTER)
        await ctx.send(embed=embed)

    @commands.command(name="qualifying")
    async def f1_latest_qualifying(self, ctx):
        fields = []
        data = f1data.f1_latest_qualifying()
        race_name = data["MRData"]["RaceTable"]["Races"][0]["raceName"]

        for results in data["MRData"]["RaceTable"]["Races"][0]["QualifyingResults"]:
            position = results["position"]
            driver_code = results["Driver"]["code"]
            teamname = results["Constructor"]["name"]
            icon = ""

            if teamname.lower() in constructor_icons:
                icon = constructor_icons[teamname.lower()]

            Q1, Q2, Q3 = "", "", ""
            if "Q1" in results:
                Q1 = results["Q1"]
            if "Q2" in results:
                Q2 = results["Q2"]
            if "Q3" in results:
                Q3 = results["Q3"]

            fields.append(
                [
                    f"{icon} **{position}**: {driver_code}",
                    f"Q1: {Q1}{config.NL}Q2: {Q2}{config.NL}Q3: {Q3}",
                ]
            )

        embed = EmbedWithFields(
            title=f"{config.F1_LOGO} Qualifying Results {race_name}",
            color=0xDB1921,
            description=f"Qualifying results for the most recent {race_name}",
            fields=fields,
        )
        embed.set_footer(text=config.BOT_FOOTER)
        await ctx.send(embed=embed)

    @commands.command(name="drivers")
    async def f1_drivers(self, ctx):
        fields = []
        data = f1data.f1_drivers_all()
        for race in data["MRData"]["DriverTable"]["Drivers"]:
            first_name = race["givenName"]
            last_name = race["familyName"]
            number = race["permanentNumber"]
            code = race["code"]

            fields.append(
                [
                    f"{config.F1_LOGO}** {first_name} {last_name}**",
                    f"Number: {number}{config.NL}Code: {code}",
                ]
            )

        embed = EmbedWithFields(
            title=f"Formula 1 Driver List {f1data.year}",
            color=0xDB1921,
            description=f"The current {f1data.year} Formula 1 driver list",
            fields=fields,
        )
        embed.set_footer(text=config.BOT_FOOTER)
        await ctx.send(embed=embed)

    @commands.command(name="driver")
    async def f1_driver(self, ctx, arg):
        data = f1data.f1_driver_info(name=arg)

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
                title=f"{config.F1_LOGO} {first_name} {last_name}",
                description=f"**Number:** {number}{config.NL}**Code:** {code}{config.NL}**DOB**: {dateofbirth}{config.NL}**Nationality:** {nation}{config.NL}  [{first_name} {last_name} on Wikipedia]({url})",
                color=0xDB1921,
            )

            if last_name.lower() in driver_images:
                embed.set_thumbnail(url=driver_images[last_name.lower()])

            embed.set_footer(text=config.BOT_FOOTER)
            await ctx.send(embed=embed)

    @commands.command(name="teams")
    async def constructors(self, ctx):
        fields = []
        data = f1data.f1_team_all()

        for team in data["MRData"]["ConstructorTable"]["Constructors"]:
            name = team["name"]
            nation = team["nationality"]
            url = team["url"]
            icon = ""

            if name.lower() in constructor_icons:
                icon = constructor_icons[name.lower()]

            fields.append(
                [f"{icon} **{name}**", f"Origin: {nation}{config.NL}[More info]({url})"]
            )

        embed = EmbedWithFields(
            title=f"Formula 1 Team List {f1data.year}",
            color=0xDB1921,
            description=f"The current {f1data.year} Formula 1 team list",
            fields=fields,
        )
        embed.set_footer(text=config.BOT_FOOTER)
        await ctx.send(embed=embed)

    @commands.command(name="team")
    # gets specific constructor information
    async def constructor(self, ctx, arg):
        data = f1data.f1_team_info(name=arg)

        for team in data["MRData"]["ConstructorTable"]["Constructors"]:
            name = team["name"]
            nation = team["nationality"]
            url = team["url"]

            if name.lower() in constructor_icons:
                icon = constructor_icons[name.lower()]

            embed = discord.Embed(
                title=f"{icon} {name}",
                description=f"**Origin:** {nation}{config.NL} [{name} on Wikipedia]({url})",
                color=0xDB1921,
            )

            if name.lower() in constructor_images:
                embed.set_thumbnail(url=constructor_images[name.lower()])

            embed.set_footer(text=config.BOT_FOOTER)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(formulaOneCommands(commands))
