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
        description=f"Command Prefix = {config.BOT_PREFIX}",
        fields=[
            [
                "latestresults",
                "say soemthign here",
            ]
        ],
    )
    embed.set_footer(text=config.BOT_FOOTER)
    await ctx.send(embed=embed)


bot.run(config.BOT_KEY)
