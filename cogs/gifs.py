from discord.ext import commands


class gifs(commands.Cog):
    @commands.command(name="f1gif")
    async def f1gif(self, ctx):
        gif_data = formula1data().getrandomf1gif()
        url = gif_data["data"]["bitly_gif_url"]
        await ctx.send(url)


def setup(bot):
    bot.add_cog(gifs(commands))
