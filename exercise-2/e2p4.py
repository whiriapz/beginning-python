"""
4.	A shop is offering 15% discount on all purchases.
 Write a program which will calculate the discount and the final price given the full price of the purchases.
 The output should list the initial price,
  the discount and the final price with sensible labels.
"""

total = float(input("what is the total cost\n"))
discount = total * 0.15
final = total - discount
print("initial price $", total )
print("discount: $", round (discount, 2))
print("final price: $", round (final, 2))


# Good work!
