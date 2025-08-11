#Print 1 to N with Fizz for 3, Buzz for 5, FizzBuzz for both.
import math
number = int(input("Enter the number:"))
i = 0
for i in range(1,number+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else :
        print(i)
    i += 1 
