#!/usr/bin/python3

import MySQLdb
import sys

# This is used to get the MySQL username, password and database from the user input
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

# A way to connect to the database given
conn = MySQLdb.connect(host='localhost',
        port=3306,
        user=username,
        password=password,
        db=database)

# A cursor object
cursor = conn.cursor()

# execute a SELECT statement that gets all states from the database
cursor.execute('SELECT * FROM states ORDER BY states.id ASC')

# Print the results found
print('ID\tName')
for row in cursor:
    print(f'{row[0]}\{row[1]}')

# Close the connection
conn.close()
