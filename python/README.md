# Cool features of python

## Gatling features:

Python 2 isn't supported since january 1st 2020.

---
From a base to another one:
```python
>>> bin(10)
0b1010
>>> hex(10)
0xa
>>> oct(10)
0o12
>>> int(0xa, 16)
10
```

---
Protection of fields in classes:
```python
class Foo():
    __yeet = 1   # private attribute
    _yoot = 2    # protected attribute

    def __bar(): # private method
        pass
```

---
Get ascii value of character and vice-versa
```python
>>> ord('a')
97
>>> chr(97)
'a'
```

---
Return multiple elements in a single return statement:
```python
def returnMany():
    return 1, 2, 3, 4

a, b, c, d = returnMany()
```

---
Split a string:
```python
>>> "hello world".split(" ")
['hello', 'world']
```

---
Define explicitly types in function:
```python
def add(a: int, b: int = 0) -> int:
    return a + b
```

---
Create a string from a list with separator between each elements
```python
>>> ", ".join(["Daleks", "Cybermen", "The Master"])
'Daleks, Cybermen, The Master'
```

-------------------------------------------------------------------------------

## Some cool features

virtualenv:
```
python -m venv env
```



while/else:
while-loop: enter when condition is false
for-loop: enter when iterator is exhausted


Generator:
create a function (or class) that behave like an iterator
list comprehension = generator wrapped in a list constructor


Decorators:
pas la même chose que le DecoratorPattern
permet de modifier des fonctions et méthodes en figeant la fonction

simple methode:
in a.foo(), a is bound to foo

class method:
A is bound to foo


operator overloading
list comprehension
iterators
operateur *
zip, enumerate
