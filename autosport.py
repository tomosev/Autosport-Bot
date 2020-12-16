import discord
from discord.ext import commands
import config
from embeds import EmbedWithFields
from discord.ext.commands import CommandNotFound

bot = commands.Bot(command_prefix=config.BOT_PREFIX)


@bot.event
async def on_ready():
    print(f"Lights out, and away we go! {round(bot.latency * 1000)} {len(bot.guilds)}")
    game = discord.Game("in the paddock")
    await bot.change_presence(activity=game)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(
            ":triangular_flag_on_post: Command not found. Use F1 help for a list of commands"
        )
    raise error


bot.remove_command("help")
bot.load_extension("cogs.f1")


bot.run(config.BOT_KEY)
