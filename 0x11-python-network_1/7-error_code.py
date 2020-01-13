#!/usr/bin/python3
""" Imports """
import requests
from sys import argv
from requests import get
from requests.exceptions import RequestException


def main(host):
    """ Takes in a URL, sends a request to the URL
        and displays the body of the response.
    """
    URL = host
    req = get(URL)

    try:
        req.raise_for_status()
        text = req.text
        print('{}'.format(text))
    except Exception:
        print('Error code: {}'.format(req.status_code))


if __name__ == '__main__':
    main(argv[1])
