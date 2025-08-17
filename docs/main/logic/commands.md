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
    - `save` : Function to write savefile to config.SAVE_DIR/filename.json.
    - `load` : Function to load savefile from config.SAVE_DIR/filename.json.
    - `delete` : Function to delete savefile from config.SAVE_DIR/filename.json