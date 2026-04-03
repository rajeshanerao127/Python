start = int(input("Enter start: "))
end = int(input("Enter end: "))

result = [num for num in range(start, end + 1)
          if int(num ** 0.5) ** 2 == num and sum(map(int, str(num))) < 10]

print(result)