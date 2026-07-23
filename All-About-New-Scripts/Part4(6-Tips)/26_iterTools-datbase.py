# BONUS - itertools

import itertools

lst1 = [1, 2, 3, 4, 5]
sum_list = itertools.accumulate(lst1)
print(list(sum_list))

lst2 = ['A', 'B', 'C', 'D']
chain_list = itertools.chain(lst1, lst2)
print(list(chain_list))

names = ['Tim', 'Joe', 'Bill', 'Susan', 'Jen']
show = [1, 0, 1, 0, 1]
compressed_list = itertools.compress(names, show)
print(list(compressed_list))