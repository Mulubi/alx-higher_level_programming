#!/usr/bin/python3


import MySQLdb
import sys


# get MySQL username, password and database from the inputs
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]


# create a connection to the database
conn = MySQLdb.connect(host='localhost',
                       port=3306,
                       user=username,
                       password=password,
                       db=database)


# create a cursor object
cursor = conn.cursor()


# execute a SELECT statement to get all states from the database
# that have names starting with the letter N
cursor.execute('SELECT * FROM states WHERE name LIKE "N%"' +
               'ORDER BY states.id ASC')


# print the results
for row in cursor:
    print({}, '{}'.format(row[0], row[1]))

# close the connection
conn.close()
