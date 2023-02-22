"""
1.	A curtain company charges $6.50 per metre to make up a set of curtains and $45 to install them. Write a program which will store:
•	the cost of the material per metre
•	the number of metres the user requires required
and will output:
•	the total cost of the cloth used for the curtains
•	the cost of making the cloth into curtains
•	the total cost of the curtains, including installation
the output should have descriptive text to explain the amount shown.

"""

cpm = int(input("how much is your cloth per m? "))
m_required = int(input("how many meters do you need? "))

cost_of_cloth = m_required + m_required

cost_labor = m_required * 6.50

total_cost = cost_labor + cost_of_cloth + 45

print("cost of cloth", cost_of_cloth)
print("cost of labor", cost_labor)
print("total cost", total_cost)