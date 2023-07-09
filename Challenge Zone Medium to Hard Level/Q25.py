"""
Write a Python program to find the digits which are absent in a given mobile number.
"""
digits = "0123456789"
mobileno = input("Enter a mobile number")

if len(mobileno) == 10:
    for i in digits:
        if i not in mobileno:
            print(f"{i} is not in the entered mobile number")
else:
    print("PLease enter a valid mobile number")
