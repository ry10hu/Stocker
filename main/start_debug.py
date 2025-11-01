#!/usr/bin/env python

import threading
# from gui.main import MainApp
from logic.loops import loop
import logic.commands as commands

commands.transactions.sell("GOOGL", 10.0, "ry10hu")