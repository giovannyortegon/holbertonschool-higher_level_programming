#!/usr/bin/python3

from urllib.request import Request, urlopen


def main():
    req = Request('https://intranet.hbtn.io/status')
    with urlopen(req) as response:
        text = response.read()

    print('Body response:')
    print('\t- type: {}'.format(type(text)))
    print('\t- content: {}'.format(text))
    print('\t- utf8 content: {}'.format(text.decode('utf-8')))


if __name__ == '__main__':
    main()
