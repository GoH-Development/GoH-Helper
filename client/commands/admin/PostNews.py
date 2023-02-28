#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Importing disnake

import disnake 
from disnake.ext import commands 

# Importing client path

from client import config

# Importing ui

from client.ui.NewsModal import NewsModal

class PostNews(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.slash_command(name = "postnews")
    @commands.has_permissions(administrator = True)
    async def sendtemp(self, inter: disnake.ApplicationCommandInteraction):
        """
        Post news
        """
        await inter.response.send_modal(NewsModal())


def setup(client):
    client.add_cog(PostNews(client))