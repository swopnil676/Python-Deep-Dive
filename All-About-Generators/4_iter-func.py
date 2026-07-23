x = range(1, 11)

it = iter(x)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
for i in it:
    print(i)
    