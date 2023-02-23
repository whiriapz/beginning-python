"""
5.	A furniture shop charges $89 for chairs and $148 for desks.
 Write a program to calculate the total cost when a customer purchases any number of desks and chairs.
  The output should have sensible text descriptions.
"""
chairs = int(input("how many chairs you want\n"))
tables = int(input("how many tables you want\n"))
total = (chairs * 89) + (tables * 148)

print(" cost of chairs is $",chairs * 89)
print("cost of desks is $",tables * 148)
print("total cost is $",total)

# Good work!
