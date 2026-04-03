string=input("Enter a string:")
result = ''.join([string[i] for i in range(len(string)) if i%3 !=0])
print(result)