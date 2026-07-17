strings = ["my","world","apple","pear"]

# lengths = map(len, strings)
# lengths = map(lambda x: x + "s", strings)

def add_S(string):
    return string + "s"
lengths = map(add_S, strings)

print(list(lengths))
