def leap_year():
    year = int(input("Please enter the year "))
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")


leap_year()
