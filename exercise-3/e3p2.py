"""
2.	Write a program that will input someone’s age and print out either
 “You are not old enough to vote” or “You are old enough to vote” 
 depending on whether they are 18 or not.
"""

age = int(input("how old are you \n"))
if age >= 18:
    print("you are old ehnough to vote")
else:
    print("you are not old enough to vote")