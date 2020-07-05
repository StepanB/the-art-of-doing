# Basic Data Types Challenge 4: Right Triangle Solver App

import math

# print welcome message
print("Welcome to the Right Triangle Solver App\n")

# get length of first leg
first_leg = float(input("What is the first leg of the triangle: "))

# get length of second leg
second_leg = float(input("What is the second leg of the triangle: "))

# calculate hypotenuse and area
hypotenuse = round(math.sqrt(first_leg**2 + second_leg**2), 3)
area = round((first_leg*second_leg)/2, 3)

# print both
print(f"\nFor a triangle with legs o {first_leg} and {second_leg} the hypotenuse is {hypotenuse}.")
print(f"For a triangle with legs o {first_leg} and {second_leg} the area is {area}.")
