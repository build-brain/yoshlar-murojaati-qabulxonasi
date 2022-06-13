import sqlite3


con = sqlite3.connect('database.db')
cur = con.cursor()

# Insert a row of data
insert_script = "INSERT INTO DATA (name, phone, address, date, text) VALUES (%s, %s, %s, %s, %s)"
