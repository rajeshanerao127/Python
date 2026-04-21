# Bowling pins problem

n = int(input("Enter number of pins: "))
k = int(input("Enter number of balls: "))

pins = ['I'] * n

for _ in range(k):
    start, stop = map(int, input("Enter range (start stop): ").split())
    for i in range(start - 1, stop): 
        pins[i] = '.'

print(''.join(pins))