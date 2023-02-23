"""
6.	Write a program which will ask for three numbers, save them in three different variables and will then print out the three numbers, the total and the average in the following format:

The numbers were ___, ____ and _____
The total of these numbers is ___________
The average of these numbers is _____________


"""
num1 = int(input("what is your first number " ))
num2 = int(input("what is your second number " ))
num3 = int(input("what is your third number " ))
total = num1 + num2 + num3
print(f"the three numbers were {num1}, {num2} and {num3}" ) 
print(f"the total of the numbers is {num1} + {num2} + {num3}")
print(f"the average of the three numbers is {round(total/3, 2)}")

# Good work!
