#✅  Checking for a Leap Year , 2024 → Yes

#Leap day occurs in each year that is a multiple of 4, except for years evenly divisible by 100 but not by 400.

year = int(input("Enter year \n"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(year,"is a leap year")
else:
    print(year,"isn't a leap year")