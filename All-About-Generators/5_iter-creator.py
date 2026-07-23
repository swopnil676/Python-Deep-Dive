import sys

class Iter:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.current = -1
        return self

    def __next__(self):
        self.current += 1

        if self.current >= self.n:
            raise StopIteration

        return self.current


X = Iter(5)
itr = iter(X)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

for i in X:
    print(i)