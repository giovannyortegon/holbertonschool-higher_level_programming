#!/usr/bin/env python3

import MySQLdb
from sys import argv


def connect():
    if len(argv) == 4:
        conn = MySQLdb.connect(host='localhost', user=argv[1],
                               passwd=argv[2], db=argv[3], port=3306)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM states ORDER BY id ASC;')

        for row in cursor.fetchall():
            print(row)

        conn.close()


if __name__ == '__main__':
    connect()
