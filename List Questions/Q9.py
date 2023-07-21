'''
9. Write a Python program to clone or copy a list. 

'''

n=int(input('enter the length:'))
mylist=[int(input('enter the number:')) for i in range(n)]
print(mylist)

newlist=mylist.copy()
print(newlist)