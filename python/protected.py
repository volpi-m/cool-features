#!/usr/bin/env python

class Yah():

    def __init__(self):
        print("Constructor")
        self.__ouais = 1
        self.name = "ouais"

    def __pute(self):
        print("Pute")

def main():
    a = Yah()
    print(a.name)

if __name__ == "__main__":
    main()