#check the give number is perfect or not
num = int(input("Please enter the number : "))
sum = 0
for i in range(1,int((num/2)+1)):
    if num % i == 0:
        sum = sum+i
if sum == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is a not perfect number")