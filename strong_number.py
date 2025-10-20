#Check if a number is an strong number.
num = int(input("Please enter the number : "))
temp = num 
total = 0
while temp>0:
    digit = temp % 10
    fact = 1
    for i in range(1,digit+1):
        fact = fact * int(i)
    total = total + fact
    temp = temp // 10
if total == num :
    print(f"{num} is a strong number")
else:
    print(f"{num} is not a strong number")