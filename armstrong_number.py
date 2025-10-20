#Check if a number is an Armstrong number.
num = int(input("Please enter the number : "))
p = len(str(num))
total = 0
for i in str(num):
    m = int(i) ** int(p)
    total = int(total) + int(m)
if total == num :
    print(f"{num} is Armstrong number")
else:
    print(f"{num} is not Armstrong number")
