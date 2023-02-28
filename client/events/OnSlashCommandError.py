#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Importing disnake

import disnake 
from disnake.ext import commands 
from disnake.utils import get

# Importing client path

from client import config

class OnSlashCommandError(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.Cog.listener()
    async def on_slash_command_error(self, inter, exception):
        if isinstance(exception, commands.MissingPermissions):
            embed = disnake.Embed()
            embed.description = "> Недостаточно прав для использования подобной команды!"
            embed.color = config.HELPER['EmbedColor']
            await inter.send(embed=embed, ephemeral=True)
        if isinstance(exception, commands.BotMissingPermissions):
            embed = disnake.Embed()
            embed.description = "> У бота недостаточно прав для выполнения подобных действий"
            embed.color = config.HELPER['EmbedColor']
            await inter.send(embed=embed, ephemeral=True)
        else:
            embed = disnake.Embed()
            embed.description = f"> Произошла неизвестная ошибка! \n\n `{exception}`"
            embed.color = config.HELPER['EmbedColor']
            await inter.send(embed=embed, ephemeral=True)

def setup(client):
    client.add_cog(OnSlashCommandError(client))