import sys

def gen(n):
    """Instead create next and iter method implemented manually, instatly by gen()"""
    yield 1
    print('Pause 1')
    yield 2
    print('Pause 2')
    yield 3
    print('Pause 3')
    yield 4
    print('Pause 4')


X = gen(1)
print(next(X))
print(next(X))
print(next(X))
print(next(X))