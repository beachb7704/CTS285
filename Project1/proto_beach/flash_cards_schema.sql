DROP TABLE IF EXISTS flash_cards;

CREATE TABLE flash_cards (
    row_id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    category TEXT NOT NULL,
    num1 INTEGER NOT NULL,
    math_op TEXT NOT NULL,
    num2 INTEGER NOT NULL,
    ans INTEGER NOT NULL
);