import sqlite3

connection = sqlite3.connect('instance/mathmaticus.db')


with open('flash_cards_schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# # initialize the flash_cards.db with times 1 tables
# for i in range(11):
#     cur.execute("INSERT INTO flash_cards (category, num1, operator, num2, ans) VALUES (?, ?, ?, ?, ?)",
#                 ("times 1 tables", 1, '*', i, i)
#                 )

# # initialize the flash_cards.db with times 2 tables
# for i in range(11):
#     cur.execute("INSERT INTO flash_cards (category, num1, operator, num2, ans) VALUES (?, ?, ?, ?, ?)",
#                 ("times 2 tables", 2, '*', i, 2*i)
#                 )
    
# setting up category names to the times 0-10 tables  
cat_names = []  
for i in range(11):
    cat_names.append("times " + str(i) + " tables")

# initialize the flash_cards.db with times 0-10 tables
for i in range(11):
    for j in range(11):
        cur.execute("INSERT INTO flash_cards (category, num1, operator, num2, ans) VALUES (?, ?, ?, ?, ?)",
                (cat_names[i], i, '*', j, j*i)
                )

connection.commit()
connection.close()