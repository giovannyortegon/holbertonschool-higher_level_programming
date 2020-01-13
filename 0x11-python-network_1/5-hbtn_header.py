#!/usr/bin/python3
""" Imports """
from sys import argv
from requests import get


def main(url):
    """ Fetches https://intranet.hbtn.io/status
    """
    req = get(url)
    text = req.headers['X-Request-Id']
    print('{}'.format(text))


if __name__ == '__main__':
    main(argv[1])
