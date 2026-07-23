# 1. lower() - Convert string to lowercase
print("Hello".lower())  # Output: 'hello'

# 2. upper() - Convert string to uppercase
print("Hello".upper())  # Output: 'HELLO'

# 3. strip() - Remove leading and trailing spaces
print(" hi ".strip())  # Output: 'hi'

# 4. split() - Split string by separator
print("a,b,c".split(','))  # Output: ['a', 'b', 'c']

# 5. join() - Join elements with a separator
print("-".join(['a', 'b', 'c']))  # Output: 'a-b-c'

# 6. replace() - Replace a substring
print("hello".replace('l', 'x'))  # Output: 'hexxo'

# 7. find() - Find index of substring
print("hello".find('e'))  # Output: 1

# 8. count() - Count occurrences of substring
print("banana".count('a'))  # Output: 3

# 9. startswith() - Check if string starts with prefix
print("hello".startswith('he'))  # Output: True

# 10. endswith() - Check if string ends with suffix
print("hello".endswith('lo'))  # Output: True

# 11. isalpha() - Check if all characters are letters
print("abc".isalpha())  # Output: True

# 12. isdigit() - Check if all characters are digits
print("123".isdigit())  # Output: True

# 13. isalnum() - Check if all characters are letters or digits
print("abc123".isalnum())  # Output: True

# 14. title() - Convert to title case
print("hello world".title())  # Output: 'Hello World'

# 15. capitalize() - Capitalize first character
print("python".capitalize())  # Output: 'Python'

# 16. swapcase() - Swap uppercase to lowercase and vice versa
print("PyThOn".swapcase())  # Output: 'pYtHoN'

# 17. center() - Center string with fill character
print("hi".center(6, '*'))  # Output: '**hi**'