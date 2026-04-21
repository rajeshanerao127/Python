# First timestamp
h1 = int(input("Enter first timestamp hours: "))
m1 = int(input("Enter first timestamp minutes: "))
s1 = int(input("Enter first timestamp seconds: "))

# Second timestamp
h2 = int(input("Enter second timestamp hours: "))
m2 = int(input("Enter second timestamp minutes: "))
s2 = int(input("Enter second timestamp seconds: "))

# Convert to total seconds
time1 = h1 * 3600 + m1 * 60 + s1
time2 = h2 * 3600 + m2 * 60 + s2

difference = time2 - time1

print(f"Difference: {difference} seconds")