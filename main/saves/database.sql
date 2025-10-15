PRAGMA foreign_keys = ON;

-- Team owns players > players own inventory > inventory owns items/stocks


CREATE TABLE players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    player_name TEXT NOT NULL UNIQUE,
    cash FLOAT NOT NULL,
    team_id INTEGER,
    FOREIGN KEY (team_id) REFERENCES teams (id) ON DELETE SET NULL
);


CREATE TABLE teams (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    team_name TEXT NOT NULL UNIQUE
);

CREATE TABLE stocks (
    stock_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    stock_name TEXT NOT NULL UNIQUE,
    stock_desc TEXT NOT NULL,
    price FLOAT NOT NULL
);

CREATE TABLE inventory (
    player_id INTEGER NOT NULL,
    stock_id INTEGER NOT NULL,
    amount INTEGER NOT NULL,
    PRIMARY KEY (player_id, stock_id),
    FOREIGN KEY (player_id) REFERENCES players (player_id) ON DELETE CASCADE,
    FOREIGN KEY (stock_id) REFERENCES stocks (stock_id) ON DELETE CASCADE
);





INSERT INTO stocks (stock_name, stock_desc, price) VALUES ('AAPL', 'Apple Inc.', 150.0);

INSERT INTO players (player_name, cash) VALUES ('ry10hu', 1000.0);

INSERT INTO inventory (player_id, stock_id, amount) VALUES ((SELECT player_id FROM players WHERE player_name = 'ry10hu'), (SELECT stock_id FROM stocks WHERE stock_name = 'AAPL'), );
