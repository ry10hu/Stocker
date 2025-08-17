[AssetTab.py](../../../main.gui/AssetTab.py)
-
File that contains the gui for the Assets tab

Breakdown: <br>
 - `AssetPanedWindow` : Divider for the Graph and ListBox
 - `AssetListBox` : List Box widget for selecting asset to view
 - `BuyButton` : Button widget to buy asset (amount determined by AssetAmountEntry)
 - `SellButton` : Button widget to sell asset (amount determined by AssetAmountEntry)
 - `AssetAmountEntry` : Entry widget for sell/buy amount of assets
 - `TotalTextBox` : Text widget to show total (asset price * AssetAmountEntry)
 - `MPLPlaceholderFrame` : Frame widget placeholder for MatPlotLib graph