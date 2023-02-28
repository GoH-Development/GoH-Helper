#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import listdir 
from typing import List

from client import config

def get_buttons(inter, string: str) -> List[str]:
    
    list = config.BUTTONS.keys()    

    string = string.lower()
    return [btns for btns in list if string in btns.lower()]