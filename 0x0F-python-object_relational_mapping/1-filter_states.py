#!/usr/bin/python3
"""
Script that lists all states with a name 
starting with `N` from the
database `hbtn_0e_0_usa`
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    connecting to the database to retrieve the specified states
    """
    db_conn = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_cursor = db_conn.cursor()

    db_cursor.execute(
    "SELECT * FROM states WHERE states.name LIKE BINARY 'N%' \
            ORDER BY states.id ASC")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
