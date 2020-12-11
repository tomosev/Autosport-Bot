import discord
from discord.ext import commands
from embeds import nl, bot_name
from dotenv import load_dotenv
import os


bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Green flag'.format(commands))


bot.remove_command('help')
bot.load_extension("cogs.gifs")
bot.load_extension("cogs.f1commands")

# fix desc, must be a better way


@bot.command(name="help")
async def helpcommand(ctx):
    desc = f"Command prefix `!`{nl}{nl}**f1latestresults**{nl}Lists the latest race results.{nl}{nl}**f1qualifying**{nl}Lists the latest qualifying results with Q1, 2 & 3 lap times.{nl}{nl}**f1driverstandings**{nl}Lists the current driver standings.{nl}{nl}**f1teamstandings**{nl}List the current constructor standings.{nl}{nl}**f1calendar**{nl}Lists the current formula 1 calendar.{nl}{nl}**f1drivers**{nl}Lists the current drivers that are on the grid.{nl}{nl}**f1teams**{nl}Lists the current constructors racing for the year.{nl}{nl}**f1team** {nl}Query a specific constructor's information past or present.  `!f1team mercedes`{nl}{nl}**f1driver**{nl}Query a specific driver's information past or present.  `!f1driver hamilton`{nl}{nl}**f1gif**{nl}Get a random f1 gif in response, just for fun!"
    embed = discord.Embed(title="Autosport Bot Commands",
                          description=desc, color=0xDB1921)
    embed.set_footer(text=bot_name)
    await ctx.send(embed=embed)


load_dotenv()
KEY = os.environ.get("DISCORD_KEY")
bot.run(KEY)
