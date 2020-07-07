# print welcome message
print("Welcome to the Favorite Teachers Program\n")

# get four teachers name
teachers = []
teachers.append(input("Who is your first favorite teacher: ").title())
teachers.append(input("Who is your second favorite teacher: ").title())
teachers.append(input("Who is your third favorite teacher: ").title())
teachers.append(input("Who is your forth favorite teacher: ").title())

# sort teachers by rank, alphabetically, reverse alphabetically
print(f"\nYour favorite teachers ranked are: {teachers}")
print(f"Your favorite teachers alphabetically are: {sorted(teachers)}")
print(f"Your favorite teachers reverse alphabetically order are: {sorted(teachers, reverse=True)}")

# print teachers by two, the last one and number of them
print(f"\nYour top two teachers are: {teachers[0]} {teachers[1]}.")
print(f"Your next two teachers are: {teachers[2]} {teachers[3]}.")
print(f"Your last favorite teacher is: {teachers[-1]}.")
print(f"You have a total of {len(teachers)} favorite teachers.")

# print info about no longer favorite teacher
teachers\
    .insert(0,
            input(f"\nOops, {teachers[0]} is no longer your first favorite teacher. Who is your new FAVORITE teacher: ")
            .title())

# print updated info
print(f"\nYour favorite teachers ranked are: {teachers}")
print(f"Your favorite teachers alphabetically are: {sorted(teachers)}")
print(f"Your favorite teachers reverse alphabetically order are: {sorted(teachers, reverse=True)}")

# print teachers by two, the last one and number of them
print(f"\nYour top two teachers are: {teachers[0]} {teachers[1]}.")
print(f"Your next two teachers are: {teachers[2]} {teachers[3]}.")
print(f"Your last favorite teacher is: {teachers[-1]}.")
print(f"You have a total of {len(teachers)} favorite teachers.")

# remove one teacher and print updated info
teachers\
    .remove(input("\nYou've decided you no longer like a teacher. Which teacher would you like to remove from list: ")
            .title())

print(f"\nYour favorite teachers ranked are: {teachers}")
print(f"Your favorite teachers alphabetically are: {sorted(teachers)}")
print(f"Your favorite teachers reverse alphabetically order are: {sorted(teachers, reverse=True)}")

# print teachers by two, the last one and number of them
print(f"\nYour top two teachers are: {teachers[0]} {teachers[1]}.")
print(f"Your next two teachers are: {teachers[2]} {teachers[3]}.")
print(f"Your last favorite teacher is: {teachers[-1]}.")
print(f"You have a total of {len(teachers)} favorite teachers.")