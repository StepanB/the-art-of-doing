# print welcome message
print("Welcome to the Grade Sorter App\n")

# ask for four grades and print them
grades = []
grades.append(int(input("What is your first grade: ")))
grades.append(int(input("What is your second grade: ")))
grades.append(int(input("What is your third grade: ")))
grades.append(int(input("What is your fourth grade: ")))
print(f"\nYour grades are: {grades}")

# sort grades from highest to lowest
grades.sort(reverse=True)
print(f"\nYour grades from highest to lowest are: {grades}")

# drop two lowest grades and print them
print(f"\nThe lowest two grades will now be dropped.")
print(f"Removed grad: {grades[-1]}")
grades.pop(-1)
print(f"Removed grad: {grades[-1]}")
grades.pop(-1)

# print remaining grades
print(f"\nYour remaining grades are: {grades}")

# print highest grad
print(f"Nice work! Your highest grade is a {grades[0]}")