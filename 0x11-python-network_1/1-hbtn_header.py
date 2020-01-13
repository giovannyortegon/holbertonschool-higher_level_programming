#!/usr/bin/python3
""" Imports """
from sys import argv
from urllib.request import Request, urlopen


def main(value):
    """ main  fucntion
        Customize a request to retrieve
        X-Request-Id of the page
    """
    req = Request(value)
    with urlopen(req) as response:
        text = response.getheader('X-Request-Id')

    print('{}'.format(text))


if __name__ == '__main__':
    main(argv[1])
