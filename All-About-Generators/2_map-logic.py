import sys

x = [1,2,3,4,5,6,7,8,9,10]

y = map(lambda i: i**2, x)
y = map(lambda i: i**2, range(1, 11))

print(list(y))          # Consumes the iterator

print(sys.getsizeof(y)) # Size of the map object
print(sys.getsizeof(list(y)))  # Empty list, because y is exhausted