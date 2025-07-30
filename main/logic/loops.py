#!/usr/bin/env python

import time, random, logic.commands as commands

def loop():
        
    while True:
        
        stock = str(random.choice(list(commands.files.save_r["assets"])))
        
        price = commands.files.save_r["assets"][stock]["price"]
        
        change = int(price * random.uniform(-0.01, 0.01))
        commands.files.save_r["assets"][stock]["price"] += change
    
        time.sleep(60)
