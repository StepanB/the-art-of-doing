# print welcome message
print("Welcome to the Multiplication/Exponent Table App\n")

# get user name
name = input("Hello, what is your name: ").strip().title()

# get number
number = float(input("What number would you like to work with: "))

# print multiplication table from 1 to 9
print(f"\nMultiplication Table for {number}\n")
for x in range(1, 10):
    print(f"\t{x} * {number} = {round(x*number, 2)}")

# print exponent table from 1 to 9
print(f"\nExponent Table for {number}\n")
for x in range(1, 10):
    print(f"\t{number} ** {x} = {round(number**x, 4)}")

# print user and math is cool
print(f"\n{name.title()} Math is cool!")
print(f"\t{name.lower()} math is cool!")
print(f"\t\t{name.title()} Math Is Cool!")
print(f"\t\t\t{name.upper()} MATH IS COOL!")
