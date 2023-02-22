"""
4.The gas company charges 7.45 cents per unit for the first 55 units
 of gas and 6.85 cents per unit for each extra unit of gas used.
 Write a program that will calculate a customer’s monthly account
when the number of units of gas used is entered.
 The account should be in dollars
"""
gas = float(input("how many units \n"))
if gas <= 55:
    total = gas * 7.45
    print("your bill for this month is $", round(total, 2))
else:
    total = 55 * 7.45 + (gas - 55) * 6.85
print("your bill for this month is $", round(total, 2))
