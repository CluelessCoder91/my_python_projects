year = int(input("Which year do you want to check? "))

if year % 4 == 0 and year % 100 != 0:
    print(f"{year} is a leap year.")
    if year % 100 == 0 and year % 400 == 0:
        print(f"{year} is not a leap year.")
else:
    print(f"{year} is not a leap year.")