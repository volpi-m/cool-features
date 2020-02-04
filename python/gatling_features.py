bin(10)         # 0b1010
hex(10)         # 0xa
oct(10)         # 0o12
int(0xa, 16)    # 10


class Foo():
    __yeet = 1   # private attribute
    _yoot = 2    # protected attribute

    def __bar(self): # private method
        pass


ord('a') # 97
chr(97)  # 'a'


def returnMany():
    return 1, 2, 3, 4
a, b, c, d = returnMany()


"hello world".split(" ") # ['hello', 'world']


def add(a: int, b: int = 0) -> int:
    return a + b


", ".join(["Daleks", "Cybermen", "The Master"])
# 'Daleks, Cybermen, The Master'


greetings = "H3110 W0RLD"
yeeting = "geekos" if not greetings.isalpha() else "not geekos"



