from itertools import zip_longest

list1 = [1, 2, 3]
list2 = ['a']

print(list(zip_longest(list1, list2, fillvalue='-'))) #converting to list
# [(1, 'a'), (2, '-'), (3, '-')]
