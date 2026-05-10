file = open("input.txt", "a")

text = input("Enter text to append: ")

file.write(text + "\n")

file.close()

print("Text appended successfully")