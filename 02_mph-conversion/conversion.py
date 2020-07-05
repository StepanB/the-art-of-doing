# Basic Data Types challenge 2: MPH to MPS Conversion APP

# print welcome message
print("Welcome to the MPH to MPS Conversion App.\n")

# prompt for speed in MPH
speed_mph = float(input("What is your speed in miles per hour: "))

# calculate MPS speed
speed_mps = speed_mph / 2.236934

# print speed in meter per second
print(f"\nYour speed in meters per second is {round(speed_mps, 2)}.")