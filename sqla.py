#Create SQLite3 database and table

#Import the SQLite3 library

import sqlite3

#create a new database if one doesn't already exist
conn = sqlite3.connect("new.db")

#create a cursor object to execute SQL commands
cursor = conn.cursor()

#create a table
cursor.execute("CREATE TABLE population (city TEXT, state TEXT, population INT)")

#close the database connection
conn.close()


