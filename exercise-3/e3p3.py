"""
3.	Write a program that will ask the user to input a number.
The output should tell the user whether the number is larger or smaller
 than zero, or equal to zero.
"""
num = float(input("pick a number "))
if num > 0:
    print("your number is higher than 0")
elif num < 0:
    print("your number is lower than 0")
else:
    print("your number 0")