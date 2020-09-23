import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()


# This creates the table if it does not exist, and gives the parameters that are to be sent into it
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
# The INTEGER PRIMARY KEY will create auto-incrementing columns

cursor.execute(create_table)

# This is for creating the item database.
# The price variable is real which means a decimal
create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(create_table)

# # This will add this item with this price into the database
# cursor.execute("INSERT INTO items VALUES ('test', 10.99)")

connection.commit()

connection.close()
