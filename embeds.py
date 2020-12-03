import discord
from discord.ext import commands


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
