import sys

def gen(n):
    """Instead create next and iter method implemented manually, instatly by gen()"""
    for i in range(n):
        yield i


for i in gen(5):
    print(i)