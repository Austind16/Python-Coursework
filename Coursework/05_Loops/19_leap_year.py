# Program to check if a given year is a leap year

# Taking year as input from the user
year = int(input("Enter a year: "))

# Leap year conditions:
# 1. If a year is divisible by 400 → leap year
# 2. Else if divisible by 100 → NOT a leap year
# 3. Else if divisible by 4 → leap year
# 4. Otherwise → NOT a leap year

if year % 400 == 0:
    print(year, "is a leap year.")
elif year % 100 == 0:
    print(year, "is not a leap year.")
elif year % 4 == 0:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
