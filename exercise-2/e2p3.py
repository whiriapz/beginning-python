"""
3.	A landscape gardening firm charges $65 per tonne for topsoil
 and $25 for the use of a trailer to carry it in
  Write a program to calculate the amount paid by customers buying any amount of topsoil
   they input. This input should be saved in a variable. 
   The output should list the amount of topsoil purchased,
   the cost of the topsoil and the total cost, 
   ith suitable labels so that the user understands the bill.
"""

topsoil = int(input(" how much topsoil do you want\n"))
total = topsoil * 65  + 25

print("topsoil purchased", topsoil)
print("topsoil costs", topsoil * 65)
print("total cost is", total)

# Good work!
