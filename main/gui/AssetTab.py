import tkinter as tk
import tkinter.ttk as ttk

class AssetTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.AssetPanedWindow = ttk.Panedwindow(self, orient="horizontal")
        self.AssetPanedWindow.place(relx=0.017, rely=0.024, relheight=0.952, relwidth=0.957)

        self.AssetPanedWindow_p1 = ttk.Labelframe(self.AssetPanedWindow, width=165, text='Pane 1')
        self.AssetPanedWindow.add(self.AssetPanedWindow_p1, weight=0)
        self.AssetPanedWindow_p1.configure(text='Pane 1')

        self.AssetPanedWindow_p2 = ttk.Labelframe(self.AssetPanedWindow, text='Pane 2')
        self.AssetPanedWindow.add(self.AssetPanedWindow_p2, weight=0)
        self.AssetPanedWindow_p2.configure(text='Pane 2')

        self.AssetListBox = tk.Listbox(self.AssetPanedWindow_p1)
        self.AssetListBox.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0, bordermode='ignore')
        self.AssetListBox.configure(background="white")
        self.AssetListBox.configure(font="TkFixedFont")
        self.AssetListBox.configure(selectbackground="#d9d9d9")

        self.BuyButton = tk.Button(self.AssetPanedWindow_p2)
        self.BuyButton.place(relx=0.224, rely=0.729, height=99, width=107
		                , bordermode='ignore')
        self.BuyButton.configure(activebackground="#d9d9d9")
        self.BuyButton.configure(font="-family {Noto Sans} -size 10")
        self.BuyButton.configure(text='''Buy''')

        self.SellButton = tk.Button(self.AssetPanedWindow_p2)
        self.SellButton.place(relx=0.498, rely=0.729, height=99, width=107
                , bordermode='ignore')
        self.SellButton.configure(activebackground="#d9d9d9")
        self.SellButton.configure(font="-family {Noto Sans} -size 10")
        self.SellButton.configure(text='''Sell''')

        self.AssetAmountEntry = tk.Entry(self.AssetPanedWindow_p2)
        self.AssetAmountEntry.place(relx=0.025, rely=0.729, height=99
                , relwidth=0.189, bordermode='ignore')
        self.AssetAmountEntry.configure(background="white")
        self.AssetAmountEntry.configure(font="-family {Noto Sans Mono} -size 10")
        self.AssetAmountEntry.configure(selectbackground="#d9d9d9")

        self.TotalTextDisplay = tk.Text(self.AssetPanedWindow_p2)
        self.TotalTextDisplay.place(relx=0.771, rely=0.729, relheight=0.246
                , relwidth=0.189, bordermode='ignore')
        self.TotalTextDisplay.configure(background="white")
        self.TotalTextDisplay.configure(font="TkTextFont")
        self.TotalTextDisplay.configure(selectbackground="#d9d9d9")
        self.TotalTextDisplay.configure(wrap="word")  
        
        self.MPLPlaceholderFrame = tk.Frame(self.AssetPanedWindow_p2)
        self.MPLPlaceholderFrame.place(relx=0.0, rely=0.05, relheight=0.666
                , relwidth=1.0, bordermode='ignore')
        self.MPLPlaceholderFrame.configure(relief='groove')
        self.MPLPlaceholderFrame.configure(borderwidth="2")
        self.MPLPlaceholderFrame.configure(relief="groove")
        # Adjust sash on map event (same as original)
        self.__funcid0 = self.AssetPanedWindow.bind('<Map>', self.__adjust_sash0)

    def __adjust_sash0(self, event):
        paned = event.widget
        pos = [165, ]
        i = 0
        for sash in pos:
            paned.sashpos(i, sash)
            i += 1
        paned.unbind('<map>', self.__funcid0)
        del self.__funcid0
