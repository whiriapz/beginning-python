
dist = int(input("how far have you travelled "))
hours = int(input("howmany hours have you worked "))
parts = int(input("what is the cost of your parts "))
cost_time = hours * 60
cost_travel = dist * 1.50
total = parts + cost_travel + cost_time

print("cost of travel", cost_travel)
print("cost of labor", cost_time)
print("total cost", total)