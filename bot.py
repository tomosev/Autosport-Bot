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
# embed re-used fields
bot_name = "Motorsport Bot"
flagemoji = ":checkered_flag:"
nl = '\n'
embed = discord.Embed()


@bot.event
async def on_ready():
    print('Green flag: {0.user}'.format(bot))


@bot.command()
async def calandar(ctx):
    fields = []
    year = datetime.datetime.now().year
    data = webCollectData().apiRaceSchedule()
    for race in data["MRData"]["RaceTable"]["Races"]:
        name = race["raceName"]
        circuit = race["Circuit"]["circuitName"]
        #url = race["url"]
        unformatteddate = race["date"]
        unformattedtime = race["time"]
        time = unformattedtime[0:5]
        date = datetime.datetime.strptime(
            unformatteddate, "%Y-%m-%d").strftime("%d/%m/%Y")
        fields.append([
            f"{flagemoji}**{name}**",
            f"Date: {date}{nl}Time: {time} (zulutime) {nl}Location: {circuit}"
        ])
    embed = EmbedWithFields(
        title=f"Race Schedule {year}",
        color=0xe60000,
        description="",
        fields=fields,
    )
    embed.set_footer(text=bot_name)
    await ctx.send(embed=embed)


@bot.command()
async def driver(ctx, arg):
    data = webCollectData().apiDriverInfo(name=arg)
    for race in data["MRData"]["DriverTable"]["Drivers"]:
        first_name = race["givenName"]
        last_name = race["familyName"]
        number = race["permanentNumber"]
        code = race["code"]
        dob = race["dateOfBirth"]
        nation = race["nationality"]
        url = race["url"]
        embed = discord.Embed(title=f"{first_name} {last_name}",
                              description=f"Number: {number}{nl}Code: {code}{nl} DOB: {dob}{nl} Nationality: {nation}{nl} {url}")
        # embed.add_field(name=f"{first_name} {last_name}",
        #                 value=f"Number: {number}{nl}Code: {code}{nl} DOB: {dob}{nl} Nationality: {nation}{nl} {url}", inline=True)
        await ctx.send(embed=embed)


load_dotenv()
KEY = os.environ.get("DISCORD_KEY")
bot.run(KEY)
