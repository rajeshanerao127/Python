# Read text from file
file = open("input.txt", "r")
text = file.read()
file.close()

# Count words
words = text.split()
count = len(words)

# Write result to new file
file = open("output.txt", "w")
file.write("Word count: " + str(count))
file.close()

print("Word count written to output.txt")