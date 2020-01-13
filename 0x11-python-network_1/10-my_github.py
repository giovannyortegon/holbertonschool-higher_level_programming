#!/usr/bin/python3
""" Imports """
from sys import argv
from requests import get, put, post


def main(args):
    """ Takes your Github credentials - username and password
        and uses the Github API to display your id.
    """
    username = args[1]
    password = args[2]
    URL = 'https://api.github.com/users/{}'.format(username)

    req = get(URL, auth=(username, password))

    if req is not None:
        print(req.json().get('id'))
    else:
        print('None')


if __name__ == '__main__':
    main(argv)
