#!/usr/bin/env python

import time, commands, random

save_r = commands.save_r
assets = commands.save_r["assets"]

def loop():
        
    while True:
        
        stock = random.choice(list(assets))
        
        price = assets[stock]["price"]
        
        # change = int(price * random.randint(-.01, .05))
        change = int(price * random.uniform(-0.01, 0.01))
        assets[stock]["price"] += change

        time.sleep(60)