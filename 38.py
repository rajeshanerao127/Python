file = open("input.txt", "r")

lines = file.readlines()
count = len(lines)

file.close()

print("Number of lines:", count)