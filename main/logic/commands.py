#!/usr/bin/env python

import sqlite3
import os
import config


class transactions:
    def buy(asset_name, buy_amount, player_name):
        """Buy function to handle buying assets"""
       
        asset = asset.upper()
        files.cursor.execute(f"SELECT EXISTS(SELECT 1 FROM stocks WHERE stock_name = ?);", (asset,))
        stockExists = files.cursor.fetchone()
       
        if stockExists and stockExists[0] == 1:
            buy_amount = int(buy_amount)

            # Get stock_id and price from database
            files.cursor.execute(f"SELECT stock_id, price FROM stocks WHERE stock_name = ?;", (asset,))
            stock_data = files.cursor.fetchone()
            if stock_data:
                stock_id, price = stock_data

            # Get player_id and cash from database
            files.cursor.execute(f"SELECT player_id, cash FROM players WHERE player_name = ?;", (player_name,))
            player_data = files.cursor.fetchone()
          
            if player_data:
                player_id, player_cash= player_data
                total = price * buy_amount  # Calculate total cost
                  
                # Get amount owned
                files.cursor.execute(f"SELECT amount FROM inventory WHERE player_id = ? AND stock_id = ?;", (player_id, stock_id))
                amount_data = files.cursor.fetchone()
                if amount_data:
                    owned_amount = amount_data[0]
                # Check if the user can afford the purchase
                if player_cash >= total:
                    confirm = input(f"Buy {buy_amount} of {asset} for {total} (y/N)? ").lower()
                    if confirm == "y":
                        
                        # Check for inventory in database
                        files.cursor.execute(f"SELECT EXISTS(SELECT 1 FROM inventory WHERE player_id = ? AND stock_id = (SELECT stock_id FROM stocks WHERE stock_name = ?));", (player_id, asset))
                        inventoryExists = files.cursor.fetchone()

                        if inventoryExists and inventoryExists[0] == 1:
                            # Update existing inventory
                            files.cursor.execute("UPDATE inventory SET amount = ? WHERE player_id = ? AND stock_id = ?", (owned_amount + buy_amount, player_id, stock_id))
                        else:
                            # Create new inventory entry
                            files.cursor.execute("INSERT INTO inventory (player_id, stock_id, amount) VALUES, ?, ?, ?", (player_id, stock_id, buy_amount))
                        
                        # Deduct money from player
                        files.cursor.execute("UPDATE players SET cash = ? WHERE player_id = ?", (player_cash - total, player_id))

                        files.conn.commit()  # Commit changes to the database
                        files.conn.close()

                        
                else:
                   print(f"Not enough money. You have ${player_cash}.")
            else:
                print(f"Player {player_name} not found.")
        else:
            print(f"{asset} is not available.")

    def sell(asset_name, sell_amount, player_name):
        """Sell function to handle selling assets."""
       
        asset_name = asset_name.upper()
        files.cursor.execute(f"SELECT EXISTS(SELECT 1 FROM stocks WHERE stock_name = ?);", (asset_name,))
        stockExists = files.cursor.fetchone()
       
        if stockExists and stockExists[0] == 1:
            sell_amount = int(sell_amount)

            # Get stock_id and price from database
            files.cursor.execute(f"SELECT stock_id, price FROM stocks WHERE stock_name = ?;", (asset_name,))
            stock_data = files.cursor.fetchone()
            if stock_data:
                stock_id, price = stock_data

            # Get player_id and cash from database
            files.cursor.execute(f"SELECT player_id, cash FROM players WHERE player_name = ?;", (player_name,))
            player_data = files.cursor.fetchone()


            if player_data:
                player_id, player_cash = player_data
                total = price * sell_amount  # Calculate total cost
                                
                # Get amount owned
                files.cursor.execute(f"SELECT amount FROM inventory WHERE player_id = ? AND stock_id = ?;", (player_id, stock_id))
                amount_data = files.cursor.fetchone()
                if amount_data:
                    owned_amount = amount_data[0]
                    # Check if the user has enough stock to sell
                    if owned_amount >= sell_amount:
                        confirm = input(f"Sell {sell_amount} of {asset_name} for {total} (y/N)? ").lower()
                        if confirm == "y":
                            
                        
                            # Update existing inventory
                            files.cursor.execute("UPDATE inventory SET amount = ? WHERE player_id = ? AND stock_id = ?", (owned_amount - sell_amount, player_id, stock_id))
                            
                            # Add money to player
                            files.cursor.execute("UPDATE players SET cash = ? WHERE player_id = ?", (player_cash + total, player_id))

                            files.conn.commit()  # Commit changes to the database
                            files.conn.close()

                            
                    else:
                        print(f"Not enough stock. You have {owned_amount} {asset_name}.")
                else:
                    print(f"You do not own any {asset_name}.")
            else:
                print(f"Player {player_name} not found.")
        else:
            print(f"{asset_name} is not available.")


class miscellaneous:
    def clear():
        """Clear the terminal screen."""
        os.system("clear")

    def inventory():
        """Print the inventory."""
        print(files.save_r)


class files:
    # Load save file (read only)
    conn = sqlite3.connect(f"{config.SAVE_DIR}/saves.db")
    cursor = conn.cursor()
    # def save(filename):
    #     """Saves the file to {config.SAVE_DIR}/{input}.json)"""
    #     # confirm = input(f"Save current progress in file {filename} (y/N)? ").lower()
    #     # if confirm == "y":
    #     file = open(f"{config.SAVE_DIR}/{filename}.json", "w")
    #     json.dump(files.save_r, file, indent=6)

    # def load(filename):
    #     """Loads the file from {config.SAVE_DIR}/{input}.json"""
    #     confirm = input(f"Load progress from file {filename} (y/N)? ").lower()
    #     if confirm == "y":
    #         files.save_r = json.load(open(f"{config.SAVE_DIR}/{filename}.json", "r"))

    # def delete(filename):
    #     confirm = input(f"Delete progress in file {filename} (y/N)? ").lower()
    #     if confirm == "y":
    #         os.remove(f"{config.SAVE_DIR}/{filename}.json")


class gui:
    def fill_asset_listbox(listbox):
        """Fill the listbox with data from the save file."""
        listbox.delete(0, "end")  # Clear existing items
        
        files.cursor.execute("SELECT stock_name, price FROM stocks;")
        rows = files.cursor.fetchall()
        
        for row in rows:
            asset, price = row
            listbox.insert("end", f"{asset.upper()} - ${price}")