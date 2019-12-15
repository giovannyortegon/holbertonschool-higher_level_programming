#!/usr/bin/python3
""" Lists all states with a name starting with N """
import MySQLdb
from sys import argv


def connect():
    """ Connection Data Base """
    if len(argv) == 4:
        conn = MySQLdb.connect(host='localhost', user=argv[1],
                               passwd=argv[2], db=argv[3], port=3306)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'\
                        ORDER BY states.id ASC;")
        # Search name on the tuple
        for row in cursor.fetchall():
            if row[1][0] == 'N':
                print(row)
        # Close connection
        conn.close()


if __name__ == '__main__':
    connect()
