#!/usr/bin/env python

class Foo():

    def __init__(self, truc):
        self.quelquechose = truc

    def __add__(self, other):
        return self.quelquechose + other.quelquechose

    def __bool__(self):
        return True if self.quelquechose is not 0 else False

    def __str__(self):
        return f"Valeur = {1234 + 5678}, {self.quelquechose}"


def main():
    a = Foo(0)
    b = Foo(3)
    print(a + b)
    if a and b:
        print("YES")
    print(b)

if __name__ == "__main__":
    main()
