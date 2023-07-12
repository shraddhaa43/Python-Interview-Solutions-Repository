"""
Write a Python program to check whether every even index contains an even number and every odd index contains odd number of a given list.
"""
list1=[0,1,2,3,4,5,6]

for i in range(0,len(list1)):
    if i%2==0 and list1[i]%2!=0:
        print(False)
        break
    elif i%2!=0 and list1[i]%2==0:
        print(False)
        break
else:
    print(True)