#Print 1 to N with Fizz for 3, Buzz for 5, FizzBuzz for both.

number = int(input("Enter the number: "))

for i in range(1, number + 1):  # start from 1 to N
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
