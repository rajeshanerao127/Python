day = int(input("Enter day (1-31): "))
month = int(input("Enter month (1-12): "))
year = int(input("Enter year: "))

if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:
    print(f"{day}/{month}/{year} is valid")
else:
    print(f"{day}/{month}/{year} is invalid")
