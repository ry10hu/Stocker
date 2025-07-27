#!/usr/bin/env python


import json
import os

class transactions:
    def buy(asset, amount):
        """Buy function to handle buying assets"""
        if asset in files.save_r["assets"]:
            asset = asset.lower()
            amount = int(amount)

            # Get price and money from save
            price = files.save_r["assets"][asset]["price"]
            money = files.save_r["other"]["money"]
            total = price * amount  # Calculate total cost

            # Check if the user can afford the purchase
            if money >= total:
                confirm = input(f"Buy {amount} of {asset} for {total} (y/N)? ").lower()
                if confirm == "y":
                    files.save_r["assets"][asset]["owned"] += amount  # Add assets to owned
                    files.save_r["other"]["money"] -= total          # Deduct money
            else:
                print(f"Not enough money. You have ${money}.")
        else:
            print(f"{asset} is not available.")

    def sell(asset, amount):
        """Sell function to handle selling assets."""
        if asset in files.save_r["assets"]:
            asset = asset.lower()
            amount = int(amount)

            # Get price and owned amount from save
            price = files.save_r["assets"][asset]["price"]
            owned = files.save_r["assets"][asset]["owned"]
            total = price * amount  # Calculate total cost

            # Check if the user has at least {amount} of {asset}
            if owned >= amount:
                confirm = input(f"Sell {amount} of {asset} for {total} (y/N)? ").lower()
                if confirm == "y":
                    files.save_r["assets"][asset]["owned"] -= amount  # Deduct assets to owned
                    files.save_r["other"]["money"] += total          # Add money
            else:
                print(f"Not enough of {asset}. You own {owned}.")
        else:
            print(f"{asset} is not available.")

class miscellaneous:
    def clear():
        """Clear the terminal screen."""
        os.system("clear")

    def inventory():
        """Print the inventory."""
        print(files.save_r)

class files:
    # Load save file (read only)
    with open('saves/1.json', "r") as file:
        save_r = json.load(file)
    def save(filename):
        """Saves the file to main/saves/{input}.json (saves/{input}.json relative to this file)"""
        confirm = input(f"Save current progress in file {filename} (y/N)? ").lower()
        if confirm == "y":    
            file = open(f"saves/{filename}.json", "w")
            json.dump(files.save_r, file, indent = 6)

    def load(filename):
        """Loads the file from main/saves/{input}.json"""
        confirm = input(f"Load progress from file {filename} (y/N)? ").lower()
        if confirm == "y":
            files.save_r = json.load(open(f"saves/{filename}.json", "r"))

    def delete(filename):
        confirm = input(f"Delete progress in file {filename} (y/N)? ").lower()
        if confirm == "y":
            os.remove("saves/{filename}.json")