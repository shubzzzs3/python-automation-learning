#sum of digit
num = list(input("Enter the num (please Enter space after every number) : ").split())
Total = 0
print(num)
for ele in num:
    Total = Total + int(ele)
print(f"Sum of {num} is {Total}")
