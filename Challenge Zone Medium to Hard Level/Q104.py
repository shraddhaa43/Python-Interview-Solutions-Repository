"""
Write a Python program to create a list of the accumulating sum from a given list.
"""
list1=[1,2,3,4,5,6]
list2=[]
sum=0
for i in list1:
    sum=sum+i
    list2.append(sum)
print(list2)