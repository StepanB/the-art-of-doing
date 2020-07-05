#Basic Data Types Challenge 1: Letter Counter App

# print welcome message
print("Welcome to the Letter Counter App\n")

# prompt for user name
name = input("What is your name: ")
print(f"Hello {name.title()}!")

# prompt for message
print("I will count the number of times that a specific letter occurs in a message.")
message = input("\nPlease enter a message: ")

# prompt for letter to count
letter = input("Which letter would you like to count the occurrences of: ")

# print counter
print(f"\n{name.title()}, your message has {message.count(letter)} {letter}'s in it.")