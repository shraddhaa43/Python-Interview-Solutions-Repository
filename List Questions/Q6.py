'''
6. Write a Python program to get a list, sorted in increasing order by the last element in each 
tuple from a given list of non-empty tuples. 
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

'''
# Sample_List = [(2, 5), (1, 2), (4, 4), (2, 3), (3, 1)]


'''using lambda'''
# sorted_list=sorted(Sample_List,key=lambda x:x[-1])
# print(sorted_list)


'''using for loop'''
# my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# n=len(my_list)
# for i in range(n-1):
#     for j in range(n-i-1):
#         if my_list[j][-1]>my_list[j+1][-1]:
#             my_list[j],my_list[j+1]=my_list[j+1],my_list[j]

# print(my_list)




