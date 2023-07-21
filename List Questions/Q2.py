"""
2. Write a Python program to multiplies all the items in a list.
"""
mylist=[i for i in range(1,6)]
prod=1
for i in mylist:
    prod=prod*i
print("Product of all items of the list is: ",prod)