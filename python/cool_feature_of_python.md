Gatling feature:

Python 2 n'est plus supporté depuis le 1er janvier


```python
>>> bin(10)
0b1010
>>> hex(10)
0xa
>>> int(0xa, 16)
10
```


Protection of fields in classes:
__ = private
_ = public


```python
>>> ord('a')
97
>>> chr(97)
'a'
```
Return plusieurs elmt:
`return a, b, c, d`

"hello world".split(" ") = ["hello", "world"]

On peux mettre des types explicitement dans les fonctions python
def yeet(a: float, b: int = 0) -> int:
    return a + b

", ".join(["Nani"])

-------------------------------------------------------------------------------

venv:
python -m venv env
restricted environment where you can install modules safely


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
