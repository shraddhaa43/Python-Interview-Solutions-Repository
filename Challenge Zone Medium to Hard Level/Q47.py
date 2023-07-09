"""
Write a Python program which reads a text (only alphabetical characters and spaces.) and prints two words. The first one is the word which is arise most frequently in the text. The second one is the word which has the maximum number of letters.
Note: A word is a sequence of letters which is separated by the spaces.
Input:
A text is given in a line with following condition:
a. The number of letters in the text is less than or equal to 1000.
b. The number of letters in a word is less than or equal to 32.
c. There is only one word which is arise most frequently in given text.
d. There is only one word which has the maximum number of letters in given text.
Input text: Thank you for your comment and your participation.
Output: your participation.
"""

input_text="Thank you for your comment and your participation."
list1=input_text.split()
most_freq=""
longest=""

for i in list1:
    if len(i)>len(longest):
        longest=i
    if list1.count(i)>list1.count(most_freq):
        most_freq=i
print(most_freq," ",longest)

# print(max(len(i for i in list1)))