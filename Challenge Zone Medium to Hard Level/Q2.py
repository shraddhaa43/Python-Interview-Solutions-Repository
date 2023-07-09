"""
Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once.
"""

import itertools

list1 = ['a', 'e', 'i', 'o', 'u']
list2 = itertools.permutations(list1,5)
for i in list2:
    print("".join(j for j in i))
