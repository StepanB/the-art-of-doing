# print welcome message
print("Welcome to the Basketball Roster Program\n")

# get start roster
roster = []
roster.append(input("Who is your point guard: ").title())
roster.append(input("Who is your shooting guard: ").title())
roster.append(input("Who is your small forward: ").title())
roster.append(input("Who is your power forward: ").title())
roster.append(input("Who is your center: ").title())

# print roster table
print("\n\tYour starting 5 for the upcoming basketball season")
print(f"\t\tPoint Guard:\t\t{roster[0]}")
print(f"\t\tShooting Guard:\t\t{roster[1]}")
print(f"\t\tSmall Forward:\t\t{roster[2]}")
print(f"\t\tPower Forward:\t\t{roster[3]}")
print(f"\t\tCenter:\t\t\t\t{roster[4]}")

# print info about injury and get new player
print(f"\nOh no. {roster[2]} is injured.")
print(f"Your roster only has {len(roster)-1} players.")
roster[2] = input(f"Who will take {roster[2]}'s spot: ").title()

# print nwe roster
print("\n\tYour starting 5 for the upcoming basketball season")
print(f"\t\tPoint Guard:\t\t{roster[0]}")
print(f"\t\tShooting Guard:\t\t{roster[1]}")
print(f"\t\tSmall Forward:\t\t{roster[2]}")
print(f"\t\tPower Forward:\t\t{roster[3]}")
print(f"\t\tCenter:\t\t\t\t{roster[4]}")

# print final messages
print(f"\nGood luck {roster[2]} you will do great!")
print(f"Your roster now has {len(roster)} players.")