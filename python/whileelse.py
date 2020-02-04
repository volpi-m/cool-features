#!/usr/bin/env python

def main():
    i = 0
    while i < 10:
        print(i)
        i += 1
    else:
        print("i > 10")

    for j in range(10):
        print(j)
    else:
        print("ouais cool")

    for h in range(100):
        if h == 24:
            print(h)
            break
    else:
        print("FDP")

if __name__ == "__main__":
    main()