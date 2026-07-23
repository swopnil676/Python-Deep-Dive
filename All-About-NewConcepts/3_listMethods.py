# Initial List
my_list = [1, 2, 3]

print("Original List:", my_list)

# 1. append()
my_list.append(4)
print("\n1. append(4):", my_list)

# 2. extend()
my_list.extend([5, 6])
print("2. extend([5, 6]):", my_list)

# 3. insert()
my_list.insert(1, 99)
print("3. insert(1, 99):", my_list)

# 4. remove()
my_list.remove(2)
print("4. remove(2):", my_list)

# 5. pop()
removed_item = my_list.pop()
print("5. pop():", removed_item)
print("   List after pop:", my_list)

# 6. count()
count_99 = my_list.count(99)
print("6. count(99):", count_99)

# 7. index()
index_99 = my_list.index(99)
print("7. index(99):", index_99)

# 8. reverse()
my_list.reverse()
print("8. reverse():", my_list)

# 9. sort()
my_list.sort()
print("9. sort():", my_list)

# 10. clear()
my_list.clear()
print("10. clear():", my_list)