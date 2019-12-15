#!/usr/bin/python3
""" This function ``text_identation``
    =================================
    find the characteres '.', ':' and '?'
    and add '\n\n' in the text
"""
import doctest


def text_indentation(text):
    """ ``text_indentation``
        recive a text argument
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    text = list(text)
    n_text = []
    for i in range(0, len(text)):
        n_text.append(text[i])
        if text[i] == ' ' and text[i-1] == '.':
            n_text.append('\n\n')
        elif text[i] == ' ' and text[i-1] == ':':
            n_text.append('\n\n')
        elif text[i] == ' ' and text[i - 1] == '?':
            n_text.append('\n\n')
    print(''.join(n_text), end='')


if __name__ == '__main__':
    doctest.testfile("./tests/5-text_indentation.txt"./, verbose=False)

