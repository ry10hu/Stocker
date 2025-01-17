#!/usr/bin/env python

from main.commands import *

commands_dict = {
                # Transactions class - handles asset transactions
                "buy":transactions.buy,
                "sell": transactions.sell,
                # Miscellaneous class - no specific group
                "clear": miscellaneous.clear,
                "inventory": miscellaneous.inventory,
                # Files class - Handles all savefile interaction
                "save": files.save,
                "load": files.load,
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