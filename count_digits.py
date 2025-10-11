#Count number of digits in a number
import math
num =  int(input("Please enter the number : "))
number = num
count = 0
if number == 0 :
    count = 1
else:
    while (number > 0):
        number = number // 10
        count = count + 1
print (f"{num} has {count} digits")
