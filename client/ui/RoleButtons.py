#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Importing disnake

import disnake 
from disnake.ext import commands 

# Importing base module

from typing import List 

class RuRoleButtons(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @disnake.ui.button(emoji="⭐", custom_id="RuRoleNews")
    async def NewsBtn(self, btn: disnake.ui.Button, interaction: disnake.Interaction):
        pass 

    @disnake.ui.button(emoji="📢", custom_id="RuRoleStatus")
    async def StatusBtn(self, btn: disnake.ui.Button, interaction: disnake.Interaction):
        pass     

    @disnake.ui.button(emoji="🎉", custom_id="RuRoleGW")
    async def GWBtn(self, btn: disnake.ui.Button, interaction: disnake.Interaction):
        pass  

class EnRoleButtons(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @disnake.ui.button(emoji="⭐", custom_id="EnRoleNews")
    async def NewsBtn(self, btn: disnake.ui.Button, interaction: disnake.Interaction):
        pass 

    @disnake.ui.button(emoji="📢", custom_id="EnRoleStatus")
    async def StatusBtn(self, btn: disnake.ui.Button, interaction: disnake.Interaction):
        pass     

    @disnake.ui.button(emoji="🎉", custom_id="EnRoleGW")
    async def GWBtn(self, btn: disnake.ui.Button, interaction: disnake.Interaction):
        pass     