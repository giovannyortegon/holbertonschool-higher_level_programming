#!/usr/bin/python3
""" Imports """
from sys import argv
from requests import post


def main(value):
    """ Takes in a URL, sends a request to the URL
        and displays the body of the response.
    """
    URL = 'http://f5e914e9e9e6.20.hbtn-cod.io:5000/search_user'
#    URL = 'http://0.0.0.0:5000/search_user'
    data = {'q': value}

    req = post(URL, data=data)

    try:
        response = req.json()
        if response.get('name') is not None:
            print('[{}] {}'.format(response.get('id'), response.get('name')))
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')


if __name__ == '__main__':
    if len(argv) == 2:
        main(argv[1])
    else:
        print('No result')
