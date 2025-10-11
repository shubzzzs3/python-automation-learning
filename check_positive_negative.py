#check if the given number is positive or negative
num = int (input("Please Enter the number :"))
if num < 0 :
    print (f"{num} is negative")
elif num > 0 :
    print (f"{num} is positive")
else:
    print (f"{num} is zero")