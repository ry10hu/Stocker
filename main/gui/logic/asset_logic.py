#!/usr/bin/env python

import json, logic.commands as commands


def fill_asset_listbox(listbox):
    """Fill the listbox with data from the save file."""
    listbox.delete(0, "end")  # Clear existing items
    data = commands.files.save_r
    for asset in data["assets"]:
        owned = data["assets"][asset]["owned"]
        price = data["assets"][asset]["price"]
        listbox.insert("end", f"{asset.capitalize()}")
