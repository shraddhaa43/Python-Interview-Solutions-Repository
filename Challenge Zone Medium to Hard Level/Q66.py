"""
66. From Wikipedia, the free encyclopaedia:
A happy number is defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers, while those that do not end in 1 are unhappy numbers.
Write a Python program to check whether a number is "happy" or not.
Sample Output:
True
True
"""

num = int(input("Enter a number"))

while num!=1:
    digits=0
    while num > 0:
        digi = num % 10
        digits = digits+ (digi * digi)
        num = num // 10
    # print(digits)
    num=digits
    if 0<num<9:
        break

print(num)
if num == 1:
    print("Happy Number")
else:
    print("Not a happy number")
