#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Importing disnake

import disnake 
from disnake.ext import commands 

# Client path

from client import config
from client.handlers.ParseEmbed import parse_embed_json
from client.handlers.GetTemplates import get_templates
from client.ui.Logger import Logger

# Basic module

from os import listdir 
from typing import Union

# Client init

client = commands.Bot(
    command_prefix = commands.when_mentioned_or("h!"),
    help_command = None, 
    sync_commands_debug = True, # In future will be deprecated
    intents = disnake.Intents.all()
)

# Loading path client/commands

for filename in listdir('./client/commands'):
    if filename.endswith('.py'):
        client.load_extension(f'client.commands.{filename[:-3]}')
        Logger(f"{filename[:-3]} has been loaded", "cogs")
    else:
        if (filename != '__pycache__'):
            for file in listdir(f'./client/commands/{filename}/'):
                if file.endswith('.py'):
                    client.load_extension(f'client.commands.{filename}.{file[:-3]}')
                    Logger(f"{filename}.{file[:-3]} has been loaded", "cogs")

# Loading path client/events

for filename in listdir('./client/events'):
    if filename.endswith('.py'):
        client.load_extension(f'client.events.{filename[:-3]}')
        Logger(f"{filename[:-3]} has been loaded", "cogs")
    else:
        if (filename != '__pycache__'):
            for file in listdir(f'./client/events.{filename}/'):
                if file.endswith('.py'):
                    client.load_extension(f'client.events.{filename}.{file[:-3]}')
                    Logger(f"{filename}.{file[:-3]} has been loaded", "cogs")

# Client run

client.run(config.HELPER['Token'])