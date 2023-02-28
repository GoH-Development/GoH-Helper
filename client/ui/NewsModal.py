#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Importing disnake

import disnake 
from disnake.ext import commands


class NewsModal(disnake.ui.Modal):
    def __init__(self) -> None:
        components = [
            disnake.ui.TextInput(
                label="Заголовок",
                placeholder="Заголовок который будет указан в посте",
                custom_id="title",
                style=disnake.TextInputStyle.short,
                min_length=5,
                max_length=20,
            ),
            disnake.ui.TextInput(
                label="Содержимое",
                placeholder="Содержимое поста в новостях",
                custom_id="content",
                style=disnake.TextInputStyle.paragraph,
                min_length=5,
                max_length=1024,
            ),
        ]
        super().__init__(title="Опубликовать новость", custom_id="post_news", components=components)