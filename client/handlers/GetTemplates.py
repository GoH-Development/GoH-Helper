#!/usr/bin/python
# -*- coding: UTF-8 -*-

from os import listdir 
from typing import List

def get_templates(inter, string: str) -> List[str]:
    list = []
    for filename in listdir('./client/templates'):
        if filename.endswith('.json'):
            list.append(str(filename[:-5]))

    string = string.lower()
    return [temp for temp in list if string in temp.lower()]