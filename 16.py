list=[1,4,7,10]

even=[]
odd=[]
for i in list:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even numbers are: ", even)
print("Odd numbers are: ", odd)