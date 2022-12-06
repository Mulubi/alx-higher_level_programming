#!/usr/bin/python3
'''
A script that takes in an argument and dsiplays all values in the
states table of a database where name matches the argument.
'''

import MySQLdb
import sys


def display_tables():
    ''' Connect this input to a MySQL server '''
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    host = 'localhost'
    port = 3306

    conn = MySQLdb.connect(host=host,
                           port=port,
                           user=username,
                           passwd=password,
                           db=database)

    ''' create a cursor object '''
    cursor = conn.cursor()

    ''' Execute the SQL query required '''
    cursor.execute("SELECT * FROM states WHERE state_name='{}'
                   ORDER BY Id ASC".format(state_name))

    ''' Fetch the results found'''
    results = cursor.fetchall()

    ''' Print the results '''
    for row in results:
        print(row)


if __name__ == '__main__':
    display_tables()
