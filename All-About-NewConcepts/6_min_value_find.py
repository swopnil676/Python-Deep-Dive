# Method 1 – Using min() Function
numbers = [5, 2, 9, 1, 7]
print("Method 1 - Minimum:", min(numbers))


# Method 2 – Using for Loop
numbers = [5, 2, 9, 1, 7]

min_val = numbers[0]

for num in numbers:
    if num < min_val:
        min_val = num

print("Method 2 - Minimum:", min_val)


# Method 3 – Taking User Input
numbers = list(map(int, input("Enter numbers: ").split()))
print("Method 3 - Minimum:", min(numbers))
# User Input
#       ↓
# "10 5 3 8 1"
#       ↓ split()
# ['10', '5', '3', '8', '1']
#       ↓ map(int, ...)
# [10, 5, 3, 8, 1]
#       ↓ min()
# 1
#       ↓
# Print Output


# Method 4 – Using while Loop
numbers = [5, 2, 9, 1, 7]

i = 0
min_val = numbers[0]

while i < len(numbers):
    if numbers[i] < min_val:
        min_val = numbers[i]
    i += 1

print("Method 4 - Minimum:", min_val)


# Method 5 – Using Sorting
numbers = [5, 2, 9, 1, 7]

numbers.sort()

print("Method 5 - Minimum:", numbers[0])