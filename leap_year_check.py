# Checking if given year is leap year or not
year = int(input("PLease Enter the year :"))
if year % 400 == 0 or (year % 4 == 0 and year % 100 !=0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")