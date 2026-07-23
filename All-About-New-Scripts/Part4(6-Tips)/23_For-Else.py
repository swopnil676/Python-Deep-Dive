# Simple-life

search = [1, 2, 3, 4, 5, 6, 7]
target = 7
found = False

for element in search:
    if element == target:
        print('I found it!')
        found = True
        break
if not found:
    print('I didnot find it!')



# Professional-life

search = [1, 2, 3, 4, 5, 6, 7]
target = 8

for element in search:
    if element == target:
        print('I found it!')
        break
else:
    print('I didnot find it!')