#!/usr/bin/python3
""" Imports """
from sys import argv
from requests import post


def main(args):
    """ Fetches https://intranet.hbtn.io/status
    """
    url = args[1]
    headers = {'email': args[2]}

    req = post(url, data=headers)
    text = req.text
    print('{}'.format(text))


if __name__ == '__main__':
    main(argv)
