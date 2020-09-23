import sqlite3

path = '/Users/rodho/PycharmProjects/PyCharm-Library/REST APIs with Flask and Python/4. SQL_Database/data.db'

connection = sqlite3.connect('data.db')
# This is going to create a file called 'data.b' which is our database

cursor = connection.cursor() # This is like the cursor of the computer, it allows us to execute our queries
                             # and store the result so that we can access it

# This creates a table (query) called users with a id, username, and password columns
create_table = "CREATE TABLE users (id int, username text, password text)"
# This defines the schema (How the data is going to look)

# This executes the creation of the table
cursor.execute(create_table)

# Let's store some data
user = (1, 'jose', 'asdf')

# This is a SWL query, which inserts the user variable to the table
insert_query = "INSERT INTO users VALUES (?, ?, ?)"

cursor.execute(insert_query, user)

# Now to insert many users:

users = [
    (2, 'rolf', 'asdf'),
    (3, 'anne', 'xyz')
]

# This does it as many times as possible
cursor.executemany(insert_query, users)

# To get the data you want
select_query = 'SELECT * FROM users'
# It is going to the users table, and find every row and select the data each time
# If you did 'select_query = "SELECT id FROM users"' it would return the id of each row

for row in cursor.execute(select_query):
    print(row)
# This would go through it like a list in the given format

# This saves the work done
connection.commit()
# This is to make sure for the connection to be closed
connection.close()