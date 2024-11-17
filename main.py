#!/usr/bin/env python

import json
from commands import *

commands_dict = {"buy": buy,
                 "sell": sell,
                 "clear": clear,
                 "inventory": inventory,
                 "save": save,
                 "load": load
                 }

def user_input():
    while True:
        user_input = input("Input: ")

        user_input_split = user_input.split(" ")
        try:
            if len(user_input_split) == 1:
                commands_dict[user_input_split[0]]()
            
            elif len(user_input_split) == 2:
                arg1 = user_input_split[1]
                commands_dict[user_input_split[0]](arg1)
            
            elif len(user_input_split) == 3:
                arg1 = user_input_split[1]
                arg2 = user_input_split[2]
                commands_dict[user_input_split[0]](arg1, arg2)

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(ex).__name__, ex.args)
            print(message)