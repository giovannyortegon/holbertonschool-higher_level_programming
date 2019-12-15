#!/usr/bin/python3
""" Lists all cities of that state """
import MySQLdb
from sys import argv


def connect():
    """ Connection function to Data Base """
    if len(argv) == 4:
        # Create connection
        conn = MySQLdb.connect(host='localhost', user=argv[1],
                               passwd=argv[2], db=argv[3], port=3306)
        # Making Cursor Object for Query Execution
        cursor = conn.cursor()
        # Query to search
        query = "SELECT cities.id, cities.name, states.name\
                 FROM cities INNER JOIN states ON\
                 states.id = cities.state_id ORDER BY cities.id;"
        # Execute Query
        cursor.execute(query)
        # Search name on the tuple
        rows = cursor.fetchall()
        for cities in rows:
            print(cities)
        # Close connection
        conn.close()


if __name__ == '__main__':
    connect()
