import json
import os

# Load save file (read only)
with open('saves/1.json', "r") as file:
    save_r = json.load(file)


def buy(asset, amount):
    """Buy function to handle buying assets"""
    if asset in save_r["assets"]:
        asset = asset.lower()
        amount = int(amount)

        # Get price and money from save
        price = save_r["assets"][asset]["price"]
        money = save_r["other"]["money"]
        total = price * amount  # Calculate total cost

        # Check if the user can afford the purchase
        if money >= total:
            confirm = input(f"Buy {amount} of {asset} for {total} (y/N)? ").lower()
            if confirm == "y":
                save_r["assets"][asset]["owned"] += amount  # Add assets to owned
                save_r["other"]["money"] -= total          # Deduct money
        else:
            print(f"Not enough money. You have ${money}.")
    else:
        print(f"{asset} is not available.")

def sell(asset, amount):
    """Sell function to handle selling assets."""
    if asset in save_r["assets"]:
        asset = asset.lower()
        amount = int(amount)

        # Get price and owned amount from save
        price = save_r["assets"][asset]["price"]
        owned = save_r["assets"][asset]["owned"]
        total = price * amount  # Calculate total cost

        # Check if the user has at least {amount} of {asset}
        if owned >= amount:
            confirm = input(f"Sell {amount} of {asset} for {total} (y/N)? ").lower()
            if confirm == "y":
                save_r["assets"][asset]["owned"] -= amount  # Deduct assets to owned
                save_r["other"]["money"] += total          # Add money
        else:
            print(f"Not enough of {asset}. You own {owned}.")
    else:
        print(f"{asset} is not available.")

def clear():
    """Clear the terminal screen."""
    os.system("clear")

def inventory():
    """Print the inventory."""
    print(save_r)

def save(filename):
    """Saves the file to saves/{input}.json"""
    print(f"Filename: '{filename}'")
    file = open(f'saves/{filename}.json', "w")
    json.dump(save_r, file, indent = 6)