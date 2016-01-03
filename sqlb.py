#this module inserts data into our database

#first import SQLite library
import sqlite3

#create the connection object
conn = sqlite3.connect("new.db")

#get cursor object to execute slq commands
cursor = conn.cursor()

#insert data
cursor.execute("INSERT INTO population VALUES('New York City',\
				'NY', '8200000')")

cursor.execute("INSERT INTO population VALUES('Omaha',\
				'NE', '450000')")
				
#commit the changes
conn.commit()

#close the databse
conn.close



