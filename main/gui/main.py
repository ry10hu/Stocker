import tkinter as tk
import tkinter.ttk as ttk
from gui.AssetTab import AssetTab  # your tab frame class
from gui.MainMenuTab import MainMenuTab
import gui.shortcuts as shortcuts

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x450+1071+546")
        self.minsize(1, 1)
        self.maxsize(2727, 1512)
        self.title("Main Window")

        self.style = ttk.Style()
        self.style.theme_use('default')

        self.notebook = ttk.Notebook(self)
        self.notebook.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

        mainmenutab = MainMenuTab(self.notebook, notebook = self.notebook)
        self.notebook.add(mainmenutab, text='Main Menu')
        
        assettab = AssetTab(self.notebook)
        
        shortcuts.bind_shortcuts(self, self.notebook)
        


def start_up():
    app = MainApp()
    app.mainloop()

if __name__ == "__main__":
    start_up()


