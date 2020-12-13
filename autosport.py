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


bot.run(config.BOT_KEY)
