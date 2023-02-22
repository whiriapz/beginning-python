"""
1.	A video shop rents weekly videos for $2 each. However, if a customer rents 10 videos, they are charged $10 for the first 10 and $2 for each one above that.
Determine inputs, processing and outputs needed, and write the code.

"""
video = int(input(" how many videos are you buying? \n"))
if video >= 10:
    total = 10 * 2 + (video - 10)
    print("total price $", total)
else:
    total = video * 2
    print("total price $", total)