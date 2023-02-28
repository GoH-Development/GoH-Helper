#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Importing disnake

import disnake 
from disnake.ext import commands 

# Importing client path

from client import config

# Importing handlers

from client.handlers.GetTemplates import get_templates
from client.handlers.GetButtons import get_buttons
from client.handlers.ParseEmbed import parse_embed_json

class SendTemplate(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.slash_command(name = "sendtemplate")
    @commands.has_permissions(administrator = True)
    async def sendtemp(
        self, 
        inter, 
        template: str = commands.Param(autocomplete=get_templates), 
        button: str = commands.Param(autocomplete=get_buttons) or None
        ):
        """
        Embed templates

        Parameters
        ----------
        template: Template
        button: Buttons
        """
        await inter.send("OK", ephemeral=True)

        with open(f"client/templates/{template}.json", encoding="utf-8") as file:
            embeds = parse_embed_json(file.read())

        if button == "None":
            for embed in embeds:
                await inter.channel.send(embed=embed)
        else:
            embs = []
            for embed in embeds:    
                embs.append(embed)
            
            data = config.BUTTONS[button]
            for i in range(len(embs)):
                try:
                    await inter.channel.send(embed=embs[i], view=data[i]())
                except:
                    await inter.channel.send(embed=embs[i])

def setup(client):
    client.add_cog(SendTemplate(client))