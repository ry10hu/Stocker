#!/usr/bin/env python

import threading
import main.main as main
import main.loops as loops

threadMain = threading.Thread(target=main.user_input)
threadLoop = threading.Thread(target=loops.loop)

threadMain.start()
threadLoop.start()

threadMain.join()

threadLoop.join()