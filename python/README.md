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

    def __bar(self): # private method
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

---
Python has ternary operator:
```python
greetings = "H3110 W0RLD"
yeeting = "geekos" if containdigit(greetings) else "nor geekos"
```

---
Format your code like [PEP8](https://www.python.org/dev/peps/pep-0008/) standard by using the `black` code formatter.

Install:
```python
pip install black
```

Use:
```python
black <fileName>
```

-------------------------------------------------------------------------------

## Some cool features

### virtualenv

virtualenv is a way to create an environment separated from your global environment. Meaning you can install modules without affecting your global env. It's really useful when dealing with differents versions of a same module.

Create an env:
```
python -m venv env
```

Activate your newly created env:
```
. env/bin/activate      # works for bash based terminal
. env/bin/activate.fish # works for fish
```

Deactivate your local env:
```
deactivate
```


## else statement with loop

Enter in the else statement in a while or for loop respectively when condition is false or when iterator is exhausted.
```python
while i < 5:
    print(i)
    i += 1
else:
    print("i > 5")

for j in range(5):
    print(j)
else:
    print("Yeet")

for h in range(100):
    if h == 24:
        print(h)
        break
else:
    print("Nope")
```

Output:
```
0
1
2
3
4
i > 5
0
1
2
3
4
Yeet
24
```


## Generator

A generator is a function (or a class) that behave almost like an iterator.
You can create a generator by using the `yield` keyword (not `yeet`, be careful)
```python
def squaredNumbers(nums):
    for i in nums:
        yield i*i

for i in squaredNumbers(range(10)):
    print(i)
```


## List comprehension

List comprehension are generators passed in a list constructor (meaning those brackets: `[]`)

```python
>>> [x * x for x in range(10)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```


## Decorators

Must not be missunderstood as the Decorator design pattern.

TODO


## Operator overloading

You can overload operators for you own classes. That's the reason why you can add 2 strings.

```python
class Foo():
    def __init__(self):
        self.nb = nb

    def __add__(self, other):       # Overload the '+' overator
        return self.nb + other.nb

    def __bool__(self):             # Called when passed in a condition
        return True if self.nb != 0 else False

    def __str__(self):              # Calles when transformed to string
        return f"Number = {self.nb}"
```

You can overload many operators: `__add__`, `__sub__`, `__lt__`, `__ge__`, `__ne__` and so on.


## Itertools

Iterator based functions inspired by Haskell, APL and SML.

```python
from itertools import *
for i in count(5):
    print(i)
# Output: infinite loop printing int in ascending order starting from 5

for i in accumulate([1, 2, 3, 4, 5]):
    print(i)
# Output: 1, 3, 6, 10, 15
```


## Operateur * / (un)packing tuples

Pack a tuple is creating a tuple:
```python
a = ("Alexandre", 150, True)
```

Unpack a tuple
```python
(name, money, canVote) = a
```

The `*` operator is used to (un)pack values from a tuple
```python
>>> x, *y, z = (1, 4, 5, 2, 8, 3, 9, 0, 6, 7)
>>> x
1
>>> y
[4, 5, 2, 8, 3, 9, 0, 6]
>>> z
7
```


## zip, enumerate

Usage of zip:
```python
square = [x * x for x in range(1, 6)]
cube = [x * x * x for x in range(1, 6)]
for s, c in zip(square, cube):
    print(f"square: {s}, cube: {c}")
```

Usage of enumerate:
```python
square = [x * x for x in range(1, 6)]
for i, val in enumerate(square):
    print(f"i = {i}, val = {val}")
```

## f-strings

F-strings are the new (python 3.6) way to format string:
```python
fName = "Matteo"
lName = "Volpi"
print(f"My name is {fName} {lName}")
# Output : 'My name is Matteo Volpi'

print(f"4 + 11 = {4 + 11}")
# Output : '4 + 11 = 15'

print(f"{sum([1, 2, 3, 4, 5])}")
# Output : 15
```
