#!/usr/bin/python3
""" Imports """
from sys import argv
from requests import get, put, post


def main(args):
    """ Please list 10 commits -from the most recent to oldest -
        of the repository “rails” by the user “rails”.
    """
    repository_name = args[1]
    owner_name = args[2]
    URL = 'https://api.github.com/repos/{}/{}/commits'.format(
        owner_name, repository_name)

    req = get(URL)
    response = req.json()

    commits = response[:10]
    for commit in commits:
        code = commit.get('sha')
        author = commit.get('commit').get('author').get('name')
        print('{}: {}'.format(code, author))


if __name__ == '__main__':
    main(argv)
