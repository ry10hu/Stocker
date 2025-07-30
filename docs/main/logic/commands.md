[commands.py](../../../main/logic/commands.py)
-
Defines all of the functions that you use when playing

Breakdown: <br>
 - `transactions` (class) :
    - `buy` : Function to handle buying assets.
    - `sell` : Function to handle selling assets.
 - `miscellaneous` (class) :
    - `clear` : Function to clear the screen.
    - `inventory` : Function to print all of `save_r` (savefile).
 - `files` (class) :
    - `save` : Function to write save to main/saves/filename.json.
    - `load` : Function to load saves from main/saves/filename.json.