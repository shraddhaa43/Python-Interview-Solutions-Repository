'''
10. Write a Python   program to find the list of words that are longer than n from a given list of 
words. 
'''
mylist=[]
newlist=[]
while True:
    n=input('enter the string:')

    if n=='':
      break
    else:
       mylist.append(n)

print(mylist)

# length=int(input('enter the length'))
# for i in mylist:
#    if len(i)> length:
#       newlist.append(i)

# print(newlist)


long_words = list(filter(lambda x: len(x) > n, mylist))
print(long_words)