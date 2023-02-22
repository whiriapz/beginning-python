"""
4.	Write a program that will ask for a particular number of inches and will convert that number to cm, with an output like

______ inches is equal to _______ cm

(1 inch = 2.54 cm)

"""

inches = int(input("how many inches to convert \n"))
cm = inches * 2.54
print(f"{inches} inches is {cm}cm")