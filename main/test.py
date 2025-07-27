#!/usr/bin/env python

from commandstest import *
from tkinter import *

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


root = Tk()


root.mainloop()
Button(root, "ha", exit())
