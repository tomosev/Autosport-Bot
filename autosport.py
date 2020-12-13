import discord
from discord.ext import commands
import config
from embeds import EmbedWithFields


bot = commands.Bot(command_prefix=config.BOT_PREFIX)


@bot.event
async def on_ready():
    print("Green flag".format(commands))


bot.remove_command("help")
bot.load_extension("cogs.f1")


@bot.command(name="help")
async def helpcommand(ctx):
    # needs finishing after I fix data section
    embed = EmbedWithFields(
        title=f"{config.BOT_NAME} Commands",
        color=0xDB1921,
        description=f"Command Prefix = ` {config.BOT_PREFIX}`",
        inline_all=False,
        fields=[
            [
                "latestresults",
                "Lists the latest race results.",
            ],
            [
                "qualifying",
                "Lists the latest qualifying results with Q1, 2 & 3 lap times.",
            ],
            [
                "driverstandings",
                "Lists the current driver standings.",
            ],
            [
                "teamstandings",
                "List the current constructor standings.",
            ],
            [
                "calendar",
                "Lists the current formula 1 calendar.",
            ],
            [
                "drivers",
                "Lists the current drivers that are on the grid.",
            ],
            [
                "teams",
                "Lists the current constructors racing for the year.",
            ],
            [
                "team",
                "Query a specific constructor's information past or present.`f1 team mercedes`",
            ],
            [
                "driver",
                "Query a specific driver's information past or present. `f1 driver hamilton`",
            ],
            [
                "gif",
                "Get a random f1 gif in response, just for fun!",
            ],
        ],
    )
    embed.set_footer(text=config.BOT_FOOTER)
    await ctx.send(embed=embed)


bot.run(config.BOT_KEY)
