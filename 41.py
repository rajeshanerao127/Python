import random

# Create two 3x3 matrices
A = []
B = []

for i in range(3):
    row1 = []
    row2 = []
    
    for j in range(3):
        row1.append(random.randint(1, 9))
        row2.append(random.randint(1, 9))
    
    A.append(row1)
    B.append(row2)

print("Matrix A:")
for row in A:
    print(row)

print("\nMatrix B:")
for row in B:
    print(row)

# Addition
add = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(A[i][j] + B[i][j])
    add.append(row)

print("\nAddition:")
for row in add:
    print(row)

# Subtraction
sub = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(A[i][j] - B[i][j])
    sub.append(row)

print("\nSubtraction:")
for row in sub:
    print(row)

# Multiplication
mul = []
for i in range(3):
    row = []
    for j in range(3):
        total = 0
        for k in range(3):
            total += A[i][k] * B[k][j]
        row.append(total)
    mul.append(row)

print("\nMultiplication:")
for row in mul:
    print(row)

# Matrix details
def details(name, matrix):
    print("\n", name)
    print("Shape: 3 x 3")
    print("Dimensions: 2")
    print("Data type:", type(matrix[0][0]))
    print("Flatten:", [item for row in matrix for item in row])

details("Addition Matrix Details", add)
details("Subtraction Matrix Details", sub)
details("Multiplication Matrix Details", mul)