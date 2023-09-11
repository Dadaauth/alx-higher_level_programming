#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    f_st = None
    if length > 0:
        f_st = sentence[0]
    return length, f_st
