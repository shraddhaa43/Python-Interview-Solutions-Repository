"""
Write a Python program to create a new string with no duplicate consecutive letters from a given string.
"""
str1="Shraddha"
str2=""
str2=str2+str1[0]
for i in range(1,len(str1)):
    if str1[i]!=str1[i-1]:
        str2=str2+"".join(str1[i])
print(str2)