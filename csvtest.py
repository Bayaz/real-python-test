#csvtest.py
#import data from CSV

#import the csv library
import csv
import sqlite3

with sqlite3.connect("new.db") as conn:
	c = conn.cursor()

	#open the csv file and assign it a variable
	employees = csv.reader(open("employees.csv", "rU"))

	#create a new table called employees
	c.execute("CREATE TABLE employees(firstname TEXT, lastname TEXT)")

	#insert data from csv file into database
	c.executemany("INSERT INTO employees(firstname, lastname) values (?, ?)", employees)

#close the databse
conn.close