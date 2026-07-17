def longer_than_4(string):
    return len(string) > 4


strings = ["my", "world", "apple", "pear"]
# filtered = filter(longer_than_4, strings)
filtered = filter(lambda x: len(x) > 4, strings)
print(list(filtered))
