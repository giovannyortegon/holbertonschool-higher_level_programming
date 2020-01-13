#!/usr/bin/python3
""" Imports """
from sys import argv
from requests import get, put, post


def main(value):
    """ Takes in a string and sends a search
        request to the Star Wars API.
    """
    URL = 'https://swapi.co/api/people'
    data = {'search': value}

    req = get(URL, params=data)

    response = req.json()
    print('Number of results: {}'.format(response.get('count')))
    results = response.get('results')
    for result in results:
        print(result.get('name'))


if __name__ == '__main__':
    main(argv[1])
