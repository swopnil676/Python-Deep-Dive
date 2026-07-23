# Example 1
x = [[0 for _ in range(5)] for _ in range(5)]
print(x)


# Example 2
y = (i for i in "hello")
print(tuple(y))
y = (i for i in "hello")
print(list(y))


# Example 3
sentence = "hello my name is sam"
x = {char: sentence.count(char) for char in set(sentence)}
print(dict(x))