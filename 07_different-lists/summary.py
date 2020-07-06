# declare lists
num_strings = ['15', '100', '55', '42']
num_ints = [15, 100, 55, 42]
num_floats = [2.2, 5.0, 1.245, 0.142857]
num_lists = [[1, 2, 4], [4, 5, 6], [7, 8, 9]]

print("\t\t\tSummary Table")
# print summary of num_string list
print(f"\nThe variable num_strings is a {type(num_strings)}.\n"
      f"It contains the elements: {num_strings}\n"
      f"The element {num_strings[0]} is a {type(num_strings[0])}")

# print summary of num_ints list
print(f"\nThe variable num_ints is a {type(num_ints)}.\n"
      f"It contains the elements: {num_ints}\n"
      f"The element {num_ints[0]} is a {type(num_ints[0])}")

# print summary of num_floats list
print(f"\nThe variable num_floats is a {type(num_floats)}.\n"
      f"It contains the elements: {num_floats}\n"
      f"The element {num_floats[0]} is a {type(num_floats[0])}")

# print summary of num_lists list
print(f"\nThe variable num_lists is a {type(num_lists)}.\n"
      f"It contains the elements: {num_lists}\n"
      f"The element {num_lists[0]} is a {type(num_lists[0])}")

# sort num_strings and num_ints and print them
print("\nNow sorting num_strings and num_ints...")
num_strings.sort()
num_ints.sort()
print(f"Sorted num_strings: {num_strings}")
print(f"Sorted num_ints: {num_ints}")

print("\nString are sorted alphabetically while integers are sorted numerically!")