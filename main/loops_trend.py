#!/usr/bin/env python
# This file is a wip implementation of trends
# I'll finish it once I get GUI and a graph of prices working

import time, random, main.commands as commands

def loop():
    chance = 100
    up = False
    while True:
            
        if trend(False, chance):
            if up:

                stock = str(random.choice(list(commands.files.save_r["assets"])))
                
                price = commands.files.save_r["assets"][stock]["price"]
                
                change = int(price * random.uniform(0.01, 0.02))
                commands.files.save_r["assets"][stock]["price"] += change
            if not up:

                stock = str(random.choice(list(commands.files.save_r["assets"])))
                
                price = commands.files.save_r["assets"][stock]["price"]
                
                change = int(price * random.uniform(0.01, 0.02))
                commands.files.save_r["assets"][stock]["price"] -= change
        else:
            up = not up

        time.sleep(5)

# roll a chance first one is 100% to go up
# then decrease by like 25% for the chance
# if fails, start going down and roll a chance first one is 100% to go down
# then decrease by like 25% for the chance


def trend(first, chance):
    if first:
        return True
    if not first:
        if random.randint(1, 100) <= chance:
            return True
        else:
            return False
        
