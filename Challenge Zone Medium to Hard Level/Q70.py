"""
Write a Python program to find the longest common prefix string amongst a given array of strings. Return false If there is no common prefix.
For Example, longest common prefix of "abcdefgh" and "abcefgh" is "abc".
Sample Output:
abc
w3r
P
"""
str1="abcdefgh"
str2="abcefgh"
str3=""
for i,j in zip(str1,str2):
    if i==j:
        str3=str3+"".join(i)
    else:
        break
if str3=="":
    print("No common prefix")
else:
    print(f"Largest common prefix: {str3}")