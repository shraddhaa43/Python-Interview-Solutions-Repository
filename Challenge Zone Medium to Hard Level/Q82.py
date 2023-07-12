"""
82. Write a Python program to calculate the median from a list of numbers.
"""
list1 = [2, 3, 5, 7, 3, 8, 9, 10]

list1.sort()
print(list1)
if len(list1) % 2 == 0:
    a = len(list1) // 2
    median = (list1[a - 1] + list1[a]) / 2
else:
    a = len(list1) // 2
    median = list1[a]
print(median)
