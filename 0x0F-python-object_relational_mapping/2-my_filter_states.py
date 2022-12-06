#!/usr/bin/python3
'''
A script that takes in an argument and dsiplays all values in the
states table of a database where name matches the argument.
'''

import MySQLdb

def display_tables(username, password, database, state_name):
    ''' Connect this input to a MySQL server '''
    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=username,
                           passwd=password,
                           db=database)

    ''' create a cursor object '''
    cursor = conn.cursor()

    ''' Execute the SQL query required '''
    cursor.execute("SELECT * FROM states WHERE state_name = '{}'
    ORDER BY Id ASC".format(state_name))

    ''' Fetch the results found'''
    results = cursor.fetchall()

    ''' Print the results '''
    for row in results:
        print(row)
