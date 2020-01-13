#!/usr/bin/python3
""" Imports """
from sys import argv
from requests import get


def main(host):
    """ Fetches https://intranet.hbtn.io/status
    """
    URL = host

    req = get(URL)
    text = req.headers.get('X-Request-Id')
    print('{}'.format(text))


if __name__ == '__main__':
    main(argv[1])
