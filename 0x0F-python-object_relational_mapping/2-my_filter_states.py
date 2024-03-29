#!/usr/bin/python3
"""
script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    connecting to the database to retrieve the specified result
    """
    db_conn = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_cursor = db_conn.cursor()

    db_cursor.execute(
       "SELECT * FROM states WHERE states.name LIKE BINARY '{}' \
            ORDER BY states.id ASC".format(argv[4]))

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
