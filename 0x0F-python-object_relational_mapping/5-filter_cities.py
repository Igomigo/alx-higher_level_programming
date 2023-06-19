#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
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
       "SELECT cities.id, cities.name FROM cities JOIN states ON \
               states.id = cities.state_id WHERE states.name \
               LIKE BINARY %(name)s ORDER BY \
               cities.id ASC", {'name': argv[4]})

    rows_selected = db_cursor.fetchall()

    if rows_selected is not None:
        print(", ".join([row[1] for row in rows_selected]))
