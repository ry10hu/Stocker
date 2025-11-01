import sqlite3


class StockerDB:

    def __init__(self, db_path="database.db"):
        self.conn = sqlite3.connect(db_path)
        self.c = self.conn.cursor()
        self.c.execute("PRAGMA foreign_keys = ON;")

    def add_stock(self, stock_name, stock_desc, price):  # Adds a stock to the stocks table
        self.c.execute(
            "INSERT INTO stocks (stock_name, stock_desc, price) VALUES (?, ?, ?)",
            (stock_name, stock_desc, price),
        )

    def add_player(self, player_name, cash):  # Adds a player to the players table
        self.c.execute(
            "INSERT INTO players (player_name, cash) VALUES (?, ?)",
            (player_name, cash),
        )

    def add_to_inventory(self, player_name, stock_name, amount_change):  # Adds/subtracts/creates item in the inventory table
        # Try to update the inventory with amount_change first
        self.c.execute(
            """ 
            INSERT INTO inventory (player_id, stock_id, amount)
            VALUES (
                (SELECT player_id FROM players WHERE player_name = ?),
                (SELECT stock_id  FROM stocks  WHERE stock_name = ?),
                ?
            )
            ON CONFLICT(player_id, stock_id)
            DO UPDATE SET amount = amount + excluded.amount
        """,
            (player_name, stock_name, amount_change),
        )

        self.c.execute(
            """
            DELETE FROM inventory
            WHERE player_id = (SELECT player_id FROM players WHERE player_name = ?)
            AND stock_id  = (SELECT stock_id FROM stocks WHERE stock_name = ?)
            AND amount <= 0
        """,
            (player_name, stock_name),
        )

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()


db = StockerDB()



db.add_to_inventory(f"ry10hu", f"AAPL", 50)


db.commit()
db.close()