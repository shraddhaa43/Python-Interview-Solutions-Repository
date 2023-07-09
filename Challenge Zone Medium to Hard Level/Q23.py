"""
Write a Python program that accept a positive number and subtract from this number the sum of its digits and so on. Continues this operation until the number is positive.
"""

num = int(input("Enter a number"))
digits = 0
num1 = num
while (num != 0):
    digi = num % 10
    digits += digi
    num = num // 10
# print(digits)
while num1 > 0:
    num1 = num1 - digits
    print(num1)
