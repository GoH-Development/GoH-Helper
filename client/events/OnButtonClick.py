#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Importing disnake

import disnake 
from disnake.ext import commands 
from disnake.utils import get

# Importing client path

from client import config

class OnButtonClick(commands.Cog):
    def __init__(self, client):
        self.client = client 

    @commands.Cog.listener()
    async def on_button_click(self, inter):
        if inter.component.custom_id == "RuRoleNews":
            role = get(inter.guild.roles, id=config.COMMUNITY['News'])
            if role in inter.author.roles:
                embed = disnake.Embed()
                embed.color = config.HELPER['EmbedColor']
                embed.description = "> Вы отписались от уведомлений о важных событиях!"
                await inter.send(embed=embed, ephemeral=True)
                await inter.author.remove_roles(role)
            else:
                embed = disnake.Embed()
                embed.color = config.HELPER['EmbedColor']
                embed.description = "> Вы подписались на уведомления о важных событиях!"
                await inter.send(embed=embed, ephemeral=True)
                await inter.author.add_roles(role)

        if inter.component.custom_id == "EnRoleNews":
            role = get(inter.guild.roles, id=config.COMMUNITY['News'])
            if role in inter.author.roles:
                embed = disnake.Embed()
                embed.color = config.HELPER['EmbedColor']
                embed.description = "> You have unsubscribed from notifications about important events!"
                await inter.send(embed=embed, ephemeral=True)
                await inter.author.remove_roles(role)
            else:
                embed = disnake.Embed()
                embed.color = config.HELPER['EmbedColor']
                embed.description = "> You subscribed to notifications of important events!"
                await inter.send(embed=embed, ephemeral=True)
                await inter.author.add_roles(role)

        if inter.component.custom_id == "RuRoleStatus":
            role = get(inter.guild.roles, id=config.COMMUNITY['Status'])
            if role in inter.author.roles:
                embed = disnake.Embed()
                embed.color = config.HELPER['EmbedColor']
                embed.description = "> Вы отписались от уведомлений об статусе сервисов!"
                await inter.send(embed=embed, ephemeral=True)
                await inter.author.remove_roles(role)
            else:
                embed = disnake.Embed()
                embed.color = config.HELPER['EmbedColor']
                embed.description = "> Вы подписались на уведомления об статусе сервисов!"
                await inter.send(embed=embed, ephemeral=True)
                await inter.author.add_roles(role)

        if inter.component.custom_id == "EnRoleStatus":
            role = get(inter.guild.roles, id=config.COMMUNITY['Status'])
            if role in inter.author.roles:
                embed = disnake.Embed()
                embed.color = config.HELPER['EmbedColor']
                embed.description = "> You have unsubscribed from service status notifications!"
                await inter.send(embed=embed, ephemeral=True)
                await inter.author.remove_roles(role)
            else:
                embed = disnake.Embed()
                embed.color = config.HELPER['EmbedColor']
                embed.description = "> You have subscribed to service status notifications!"
                await inter.send(embed=embed, ephemeral=True)
                await inter.author.add_roles(role)

        if inter.component.custom_id == "RuRoleGW":
            role = get(inter.guild.roles, id=config.COMMUNITY['Giveaway'])
            if role in inter.author.roles:
                embed = disnake.Embed()
                embed.color = config.HELPER['EmbedColor']
                embed.description = "> Вы отписались от уведомлений о розыгрышах!"
                await inter.send(embed=embed, ephemeral=True)
                await inter.author.remove_roles(role)
            else:
                embed = disnake.Embed()
                embed.color = config.HELPER['EmbedColor']
                embed.description = "> Вы подписались на уведомления о розыгрышах!"
                await inter.send(embed=embed, ephemeral=True)
                await inter.author.add_roles(role)        

        if inter.component.custom_id == "EnRoleGW":
            role = get(inter.guild.roles, id=config.COMMUNITY['Giveaway'])
            if role in inter.author.roles:
                embed = disnake.Embed()
                embed.color = config.HELPER['EmbedColor']
                embed.description = "> You have unsubscribed from giveaway notifications!"
                await inter.send(embed=embed, ephemeral=True)
                await inter.author.remove_roles(role)
            else:
                embed = disnake.Embed()
                embed.color = config.HELPER['EmbedColor']
                embed.description = "> You subscribed to giveaway notifications!"
                await inter.send(embed=embed, ephemeral=True)
                await inter.author.add_roles(role)        


def setup(client):
    client.add_cog(OnButtonClick(client))