"""
5.	Write a program that asks for the length of three sides of a triangle
 and if it is a valid triangle 
   (2 sides cannot add up must be more than the third side), 
   calculates the perimeter of the triangle. 
   Otherwise it prints out an error message.
"""
s1 = float(input("how long is side 1 of the triangle "))
s2 = float(input("how long is side 2 of the triangle "))
s3 = float(input("how long is side 3 of the triangle "))
#if s1 + s2 > s3:
#    print("the perimeter of this triangle is cm", (s1 + s2 + s3,))
#else:
#    print("error invalid triangle")

if s1 + s2 - s3 > 0 and s1 + s3 - s2 > 0 and s2 + s3 - s1 > 0:
    print("the perimeter of ths triangle is ", s1 + s2 + s3)
else:
    print("error invalid triangle")