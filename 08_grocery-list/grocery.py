import datetime

# print welcome message
print("Welcome to the Grocery List App")

# print date and time
today = datetime.date.today().strftime("%m/%d")
time = datetime.datetime.now().time().strftime("%H:%M")

print(f"Current Date and Time: {today}\t{time}")

# print info about meat and cheese
grocery = ['meat', 'cheese']
print(f"You currently have {grocery[0].title()} and {grocery[1].title()} in your list\n")

# get three new items
for x in range(3):
    grocery.append(input("Type of food to add to the grocery list: ").lower())

# print new grocery list
print(f"\nHere is your grocery list:\n{grocery}")
grocery.sort()
print(f"\nHere is your grocery list sorted:\n{grocery}")

# simulation of shopping
print("\nSimulation grocery shopping...")
for x in range(3):
    print(f"\nCurrent grocery list: {len(grocery)} items\n{grocery}")
    to_remove = input("What food did you just buy: ").lower()
    grocery.remove(to_remove)
    print(f"Removing {to_remove.title()} from list...")

print(f"\nCurrent grocery list: {len(grocery)} items\n{grocery}")
no_item = grocery.pop()
print(f"\nSorry, the store is out of {no_item}.")
grocery.append(input("What food would you like instead: ").lower())

print("\nHere is what remains on your grocery list: ")
print(grocery)
