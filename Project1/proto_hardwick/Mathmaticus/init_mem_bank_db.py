import sqlite3

connection = sqlite3.connect('memory_bank.db')


with open('mem_bank_schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# User 1
cur.execute("INSERT INTO memory_bank (user_id, num1, operator, num2, ans) VALUES (?, ?, ?, ?, ?)",
            (1, 1, '+', 1, 2)
            )
cur.execute("INSERT INTO memory_bank (user_id, num1, operator, num2, ans) VALUES (?, ?, ?, ?, ?)",
            (1, 2, '+', 2, 4)
            )
cur.execute("INSERT INTO memory_bank (user_id, num1, operator, num2, ans) VALUES (?, ?, ?, ?, ?)",
            (1, 3, '+', 3, 6)
            )

# User 2
cur.execute("INSERT INTO memory_bank (user_id, num1, operator, num2, ans) VALUES (?, ?, ?, ?, ?)",
            (2, 4, '+', 4, 8)
            )
cur.execute("INSERT INTO memory_bank (user_id, num1, operator, num2, ans) VALUES (?, ?, ?, ?, ?)",
            (2, 5, '+', 5, 10)
            )
cur.execute("INSERT INTO memory_bank (user_id, num1, operator, num2, ans) VALUES (?, ?, ?, ?, ?)",
            (2, 6, '+', 6, 12)
            )

# User 3
cur.execute("INSERT INTO memory_bank (user_id, num1, operator, num2, ans) VALUES (?, ?, ?, ?, ?)",
            (3, 7, '+', 7, 14)
            )
cur.execute("INSERT INTO memory_bank (user_id, num1, operator, num2, ans) VALUES (?, ?, ?, ?, ?)",
            (3, 8, '+', 8, 16)
            )
cur.execute("INSERT INTO memory_bank (user_id, num1, operator, num2, ans) VALUES (?, ?, ?, ?, ?)",
            (3, 9, '+', 9, 18)
            )

connection.commit()
connection.close()