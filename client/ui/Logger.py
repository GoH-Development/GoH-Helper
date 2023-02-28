#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Logger:

    def __init__(self, content, type = 'log'):
        name = 'gohbot.space/team'

        if type == 'log':
            return print(f"\033[38;5;38m[{name}] \033[38;5;45m→ INFO: \033[0;0m{content}\033[0;0m")
        if type == 'warn':
            return print(f"\033[38;5;172m[{name}] \033[38;5;214m⚠ WARN: \033[0;0m{content}\033[0;0m")
        if type == 'error':
            return print(f"\033[38;5;160m[{name}] \033[38;5;196m✘ ERR: \033[0;0m{content}\033[0;0m")     
        if type == 'debug':
            return print(f"\033[38;5;45m[{name}] \033[38;5;51m⌗ DEBUG: \033[0;0m{content}\033[0;0m")           
        if type == 'ok':
            return print(f"\033[38;5;34m[{name}] \033[38;5;46m✓ OK: \033[0;0m{content}\033[0;0m")                     
        if type == 'time':
            return print(f"\033[38;5;m[{name}] \033[38;5;67m◔ TIME: \033[0;0m{content}\033[0;0m")
        if type == 'cogs':
            return print(f"\033[38;5;38m[{name}] \033[38;5;67m⌗ COGS: \033[38;5;105m{content}\033[0;0m has been loaded")