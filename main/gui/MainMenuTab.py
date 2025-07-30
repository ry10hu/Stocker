import tkinter as tk
import tkinter.ttk as ttk
from gui.AssetTab import AssetTab
class MainMenuTab(tk.Frame):
    def __init__(self, parent, notebook=None):
        super().__init__(parent)
        self.notebook = notebook

        self.MainMenuPanedWindow = ttk.Panedwindow(self, orient="horizontal")
        self.MainMenuPanedWindow.place(relx=0.017, rely=0.024, relheight=0.952, relwidth=0.957)

        self.MainMenuPanedWindow_p1 = ttk.Labelframe(self.MainMenuPanedWindow, width=165, text='Pane 1')
        self.MainMenuPanedWindow.add(self.MainMenuPanedWindow_p1, weight=0)
        self.MainMenuPanedWindow_p1.configure(text='Pane 1')

        self.MainMenuPanedWindow_p2 = ttk.Labelframe(self.MainMenuPanedWindow, text='Pane 2')
        self.MainMenuPanedWindow.add(self.MainMenuPanedWindow_p2, weight=0)
        self.MainMenuPanedWindow_p2.configure(text='Pane 2')

        self.__funcid0 = self.MainMenuPanedWindow.bind('<Map>', self.__adjust_sash0)

        self.AssetTabButton = tk.Button(self.MainMenuPanedWindow_p2)
        self.AssetTabButton.place(relx=0.075, rely=0.126, height=59, width=147, bordermode='ignore')
        self.AssetTabButton.configure(activebackground="#d9d9d9")
        self.AssetTabButton.configure(text='Assets')
        self.AssetTabButton.configure(command=self.open_asset_tab)
        
        self.AboutText = tk.Text(self.MainMenuPanedWindow_p1)
        self.AboutText.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0, bordermode='ignore')
        self.AboutText.configure(background="white")
        self.AboutText.configure(font="TkTextFont")
        self.AboutText.configure(selectbackground="#d9d9d9")
        self.AboutText.configure(wrap="word")

    def open_asset_tab(self):
        asset_tab = AssetTab(self.notebook)
        self.notebook.add(asset_tab, text="Assets")
        self.notebook.select(asset_tab)
    def __adjust_sash0(self, event):
        paned = event.widget
        pos = [165]
        i = 0
        for sash in pos:
            paned.sashpos(i, sash)
            i += 1
        paned.unbind('<map>', self.__funcid0)
        del self.__funcid0
