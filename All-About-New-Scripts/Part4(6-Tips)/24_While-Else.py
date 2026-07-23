# Professional-life

search = [1, 2, 3, 4, 5, 6, 7]
target = 8

i = 0

while i < len(search):
    element = search[i]      # Use = for assignment
    if element == target:
        print("I found it!")
        break
    i += 1                   # Increment i

else:
    print("I did not find it!")