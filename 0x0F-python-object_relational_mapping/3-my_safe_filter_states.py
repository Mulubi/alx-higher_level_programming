#!/usr/bin/python3
'''
This script takes in arguments and displays all values in the
states table of a given database where the name matches the
argument.
'''

import MySQLdb
import sys


def display_values():
    ''' get the command line arguments '''
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    host = 'localhost'
    port = 3306

    ''' create a connection to the MySQL server '''
    conn = MySQLdb.connect(host=host,
                           port=port,
                           user=username,
                           passwd=password,
                           db=database)

    ''' Create a cursor object '''
    cursor = conn.cursor()

    '''
    Define the queries using placeholders for the
    values
    '''
    query = "SELECT * FROM states WHERE name =\
            %s ORDER BY id ASC; "

    '''
    Supply values to be input in the placeholders
    in the query
    '''
    values = (state_name,)

    ''' Execute the Query '''
    cursor.execute(query, values)

    ''' Print the results '''
    for row in cursor:
        print(row)

    ''' close the connection '''
    cursor.close()


'''
Check if the script is being executed directly
or as a module
'''
if __name__ = '__main__':
    display_values()
