# for factorial of particular number
num = int(input("Enter the number : "))
fact = 1
for i in range(1,num+1):
    fact = fact * int(i)

print(f"Then Factorial of {num} is {fact}")
