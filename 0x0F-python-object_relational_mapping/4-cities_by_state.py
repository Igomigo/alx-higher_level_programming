#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
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
       "SELECT cities.id, cities.name, states.name FROM \
               cities JOIN states ON cities.state_id = states. \
               id ORDER BY cities.id ASC")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
