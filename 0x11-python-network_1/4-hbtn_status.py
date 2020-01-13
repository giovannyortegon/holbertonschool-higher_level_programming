#!/usr/bin/python3
""" Imports """
from requests import get


def main():
    """ Fetches https://intranet.hbtn.io/status
    """
    URL = 'https://intranet.hbtn.io/status'

    req = get(URL)
    text = req.text
    print('Body response:')
    print('\t- type: {}'.format(type(text)))
    print('\t- content: {}'.format(text))


if __name__ == '__main__':
    main()
