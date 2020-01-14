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
    part1 = response.get('results')
    for result in part1:
        print(result.get('name'))

    req2 = get(response.get('next'), params=data)
    response2 = req2.json()
    part2 = response2.get('results')
    for result in part2:
        print(result.get('name'))


if __name__ == '__main__':
    main(argv[1])
