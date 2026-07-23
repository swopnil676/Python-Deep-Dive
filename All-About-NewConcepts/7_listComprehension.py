# List comprehension format:
# [expression for item in iterable if condition]

# Even numbers from 1 to 10
print("Even numbers:", [x for x in range(1, 11) if x % 2 == 0])

# Square of odd numbers
print("Square of odd numbers:", [x**2 for x in range(1, 11) if x % 2 != 0])

# Names longer than 4 letters
names = ["Ava", "Emily", "Michael", "John", "Sophia"]
print("Names longer than 4 letters:", [name for name in names if len(name) > 4])

# Numbers divisible by both 2 and 3
print("Divisible by 2 and 3:", [x for x in range(1, 21) if x % 2 == 0 and x % 3 == 0])

# Simple range (no condition)
print("All numbers 0 to 4:", [x for x in range(5)])