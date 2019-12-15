#!/usr/bin/python3
""" Lists all cities of that state """
import MySQLdb
from sys import argv


def connect():
    """ Connection Data Base """
    if len(argv) == 5:
        conn = MySQLdb.connect(host='localhost', user=argv[1],
                               passwd=argv[2], db=argv[3], port=3306)
        cursor = conn.cursor()
        name = argv[4].split('\'')[0]
        # Query to search
        query = "SELECT cities.id, cities.name, states.name\
                 FROM cities INNER JOIN states ON\
                 states.id = cities.state_id WHERE states.name = '{}' ORDER BY\
                 cities.id;".format(name)
        # Execute Query
        cursor.execute(query)
        # Search name on the tuple
        rows = cursor.fetchall()
        cities = []
        for citie in rows:
            cities.append(citie[1])
        print(', '.join(cities))
        # Close connection
        conn.close()


if __name__ == '__main__':
    connect()
