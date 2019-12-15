#!/usr/bin/python3
""" Lists all states with a name starting with N """
import MySQLdb
from sys import argv


def connect():
    """ Connection Data Base """
    if len(argv) == 5:
        conn = MySQLdb.connect(host='localhost', user=argv[1],
                               passwd=argv[2], db=argv[3], port=3306)
        cursor = conn.cursor()
        name = argv[4].split('\'')[0]
        query = "SELECT * FROM states WHERE name = '{}'\
                 ORDER BY states.id ASC".format(name)
        cursor.execute(query)
        # Search name on the tuple
        rows = cursor.fetchall()
        for state in rows:
            print(state)
        # Close connection
        conn.close()


if __name__ == '__main__':
    connect()
