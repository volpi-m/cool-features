#!/usr/bin/env python

def main():
    square = [x * x for x in range(1, 6)]
    cube = [x * x * x for x in range(1, 6)]
    for s, c in zip(square, cube):
        print(f"square: {s}, cube: {c}")

    for i, val in enumerate(square):
        print(f"i = {i}, val = {val}")

if __name__ == "__main__":
    main()
