#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Importing disnake

import disnake 
from disnake.ext import commands 
from disnake.utils import get

# Importing client path

from client import config

class OnModalSubmit(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.Cog.listener()
    async def on_modal_submit(self, inter: disnake.ModalInteraction):
        if inter.custom_id == "post_news":
            title = inter.text_values['title']
            content = inter.text_values['content']
            embed = disnake.Embed()
            embed.title = str(title)
            embed.description = str(content)
            embed.color = config.HELPER['EmbedColor']
            channel = self.client.get_channel(config.CHANNELS['News'])
            if channel:
                try: await channel.send(embed=embed)
                except: pass 
            else:
                pass 

            await inter.response.send_message("OK")
          


def setup(client):
    client.add_cog(OnModalSubmit(client))