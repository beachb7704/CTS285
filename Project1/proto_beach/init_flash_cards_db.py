import sqlite3

connection = sqlite3.connect('instance/mathmaticus.db')

with open('flash_cards_schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
    
# setting up category names to the times 0-10 tables  
cat_names = []  
for i in range(11):
    cat_names.append("Times " + str(i) + " Tables")

# initialize the flash_cards.db with times 0-10 tables
for i in range(11):
    for j in range(11):
        cur.execute("INSERT INTO flash_cards (category, num1, math_op, num2, ans) VALUES (?, ?, ?, ?, ?)",
                (cat_names[i], i, '*', j, j*i)
                )

connection.commit()
connection.close()