file = open("patients.txt", "a")
name = input("Enter patient name: ")
disease = input("Enter disease: ")

file.write(name + " - " + disease + "\n")
file.close()

file = open("patients.txt", "r")
print("\nPatient Records:")
print(file.read())
file.close()