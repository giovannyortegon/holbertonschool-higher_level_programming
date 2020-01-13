#!/usr/bin/python3
""" Imports """
from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode


def main(value):
    """ takes in a URL and an email, sends a POST
        request to the passed URL with the
        email as a parameter.
    """
    URL = value[1]
    headers = {'email': value[2]}

    data = urlencode(headers)
    data = data.encode('ascii')

    req = Request(url=URL, data=data)

    with urlopen(req) as response:
        text = response.read()
        print(text.decode('utf-8'))


if __name__ == '__main__':
    main(argv)
