#!/usr/bin/python3
""" Imports """
from sys import argv
from urllib.request import Request, urlopen
from urllib.error import HTTPError


def main(value):
    """ Takes in a URL, sends a request to the URL
        and displays the body of the response.
    """
    URL = value

    req = Request(url=URL)
    try:
        with urlopen(req) as response:
            text = response.read()
            print(text.decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))


if __name__ == '__main__':
    main(argv[1])
