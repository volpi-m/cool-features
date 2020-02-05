#!/usr/bin/env python

def returnMany():
    return 1, 2, 3

def main(*args):
    print(args)
    """
    a = ("Matteo", 123, True)
    b, *_ = returnMany()
    print(b)
    (name, money, canVote) = a
    """

if __name__ == "__main__":
    main("YEET", "YOOT", "YUUT")
