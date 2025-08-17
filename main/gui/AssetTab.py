import tkinter as tk
import tkinter.ttk as ttk
import logic.commands as commands


class AssetTab(tk.Frame):
        def __init__(self, parent):
                super().__init__(parent)

                # Paned Window
                self.AssetPanedWindow = ttk.Panedwindow(self, orient="horizontal")
                self.AssetPanedWindow.place(
                        relx=0.017, rely=0.024, relheight=0.952, relwidth=0.957
                )

                # Pane 1
                self.AssetPanedWindow_p1 = ttk.Labelframe(
                        self.AssetPanedWindow, width=165, text="Pane 1"
                )
                self.AssetPanedWindow.add(self.AssetPanedWindow_p1, weight=0)
                self.AssetPanedWindow_p1.configure(text="Pane 1")

                # Pane 2
                self.AssetPanedWindow_p2 = ttk.Labelframe(self.AssetPanedWindow, text="Pane 2")
                self.AssetPanedWindow.add(self.AssetPanedWindow_p2, weight=0)
                self.AssetPanedWindow_p2.configure(text="Pane 2")

                # Asset Listbox
                self.AssetListBox = tk.Listbox(self.AssetPanedWindow_p1)
                self.AssetListBox.place(
                        relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0, bordermode="ignore"
                )
                self.AssetListBox.configure(
                        background="white",
                        font="TkFixedFont",
                        selectbackground="#d9d9d9"
                )

                # Buy Button
                self.BuyButton = tk.Button(self.AssetPanedWindow_p2)
                self.BuyButton.place(
                        relx=0.224, rely=0.729, height=99, width=107, bordermode="ignore"
                )
                self.BuyButton.configure(
                        activebackground="#d9d9d9",
                        font="-family {Noto Sans} -size 10",
                        text="Buy",
                        command=lambda: commands.transactions.buy(
                                self.AssetListBox.get(tk.ACTIVE).lower(),
                                self.AssetAmountEntry.get()
                        )
                )

                # Sell Button
                self.SellButton = tk.Button(self.AssetPanedWindow_p2)
                self.SellButton.place(
                        relx=0.498, rely=0.729, height=99, width=107, bordermode="ignore"
                )
                self.SellButton.configure(
                        activebackground="#d9d9d9",
                        font="-family {Noto Sans} -size 10",
                        text="Sell",
                        command=lambda: commands.transactions.sell(
                                self.AssetListBox.get(tk.ACTIVE).lower(),
                                self.AssetAmountEntry.get()
                        )
                )

                # Asset Amount Entry
                self.AssetAmountEntry = tk.Entry(self.AssetPanedWindow_p2)
                self.AssetAmountEntry.place(
                        relx=0.025, rely=0.729, height=99, relwidth=0.189, bordermode="ignore"
                )
                self.AssetAmountEntry.configure(
                        background="white",
                        font="-family {Noto Sans Mono} -size 10",
                        selectbackground="#d9d9d9"
                )

                # Total Text Display
                self.TotalTextDisplay = tk.Text(self.AssetPanedWindow_p2)
                self.TotalTextDisplay.place(
                        relx=0.771, rely=0.729, relheight=0.246, relwidth=0.189, bordermode="ignore"
                )
                self.TotalTextDisplay.configure(
                        background="white",
                        font="TkTextFont",
                        selectbackground="#d9d9d9",
                        wrap="word"
                )

                # Matplotlib Placeholder Frame
                self.MPLPlaceholderFrame = tk.Frame(self.AssetPanedWindow_p2)
                self.MPLPlaceholderFrame.place(
                        relx=0.0, rely=0.0, relheight=0.7, relwidth=1.0, bordermode="ignore"
                )
                self.MPLPlaceholderFrame.configure(
                        relief="groove",
                        borderwidth="2"
                )

                # Adjust sash on map event
                self.__funcid0 = self.AssetPanedWindow.bind("<Map>", self.__adjust_sash0)
                commands.gui.fill_asset_listbox(self.AssetListBox)

        def __adjust_sash0(self, event):
                paned = event.widget
                pos = [165]
                for i, sash in enumerate(pos):
                        paned.sashpos(i, sash)
                paned.unbind("<map>", self.__funcid0)
                del self.__funcid0
