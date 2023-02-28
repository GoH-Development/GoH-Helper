#!/usr/bin/python
# -*- coding: UTF-8 -*-

from json import loads 
from disnake import Embed 

def parse_embed_json(file):
    embeds = loads(file)['embeds']

    for embed in embeds:
        embed = Embed().from_dict(embed)
        yield embed 