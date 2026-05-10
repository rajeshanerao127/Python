file = open("input.txt", "r")
content = file.read()
file.close()

file2 = open("output.txt", "w")
file2.write(content)
file2.close()

print("File copied successfully.")