# 8. Write a Python program to check a list is empty or not.

mylist = [i for i in range(0, 5)]

# method 1
if len(mylist) != 0:
    print("List is not empty")
else:
    print("list is empty")

# method 2
if bool(mylist):
    print("List is not empty")
else:
    print("list is empty")
