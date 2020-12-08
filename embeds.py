import discord


f1logo = "<:F1logo:784857003225776128>"
nl = '\n'
embed = discord.Embed()
bot_name = f"Autosport Bot{nl}*NOT affiliated with autosport.com"


class EmbedWithFields(discord.Embed):
    def __init__(self, fields, inline_all=True, **kwargs):
        """Takes the discord.Embed class and allows you to define fields immediately.
        Args:
            fields: A list of pairs of strings, the name and text of each field.
            inline_all: Whether or not to inline all of the fields.
        """
        super().__init__(**kwargs)
        for field in fields:
            self.add_field(name=field[0], value=field[1], inline=inline_all)
