#Find absolute value of a number
num = int(input(" Enter the number : "))
if num > 0 :
    print(f"Aboslute valur of {num} is {num}")
else:
    num = num - (2 * num)
    print(f"Aboslute value of {num} is {num}")

"""
if num < 0:
    num = -num
    print(num)"""