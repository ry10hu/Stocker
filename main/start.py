import threading
from gui.main import MainApp
from logic.loops import loop

def start_loop():
    t = threading.Thread(target=loop, daemon=True)
    t.start()

def main():
    start_loop()
    app = MainApp()
    app.mainloop()

if __name__ == "__main__":
    main()
