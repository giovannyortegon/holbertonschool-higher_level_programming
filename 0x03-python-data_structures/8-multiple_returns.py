#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "" or sentence is None:
        return 0, None
    else:
        a = len(sentence)
        return a, sentence[0]
