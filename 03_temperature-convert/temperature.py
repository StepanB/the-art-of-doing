# Basic Data Types Challenge 3: Temperature Conversion App

# print welcome message
print("Welcome to the Temperature Conversion Program\n")

# get temperature from user
fahr = float(input("What is the given temperature in degrees Fahrenheit:\t"))

# convert F to C and K
celsius = round((fahr-32)*(5/9), 4)
kelvin = round((fahr+459.67)*(5/9), 4)

# print table with temperatures
print(f"Degrees Fahrenheit:\t\t{fahr}")
print(f"Degrees Celsius:\t\t{celsius}")
print(f"Degrees Kelvin:\t\t\t{kelvin}")
