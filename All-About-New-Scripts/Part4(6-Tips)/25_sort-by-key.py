# sort by key

lst = [[1,2],[3,4],[4,2],[-1,3],[4,5],[2,3]]

    # Methods 1
# lst.sort()
# lst.sort(reverse=True)

    # Methods 2
# sorted(lst, key=...)
# lst.sort(key=lambda x: x[1])
    
    # Methods 3
def sort_func(x):
    return x[1] + x[0]

lst.sort(key=sort_func)
print(lst)