#Find GCD of two numbers
num1 = int(input("please enter the first number : "))
num2 = int(input("please enter the second number : "))
li1 = []
li2 = []
for i in range(1,(int(num1/2)+1)):
    if num1 % i == 0:
        li1.append(i)

for i in range(1,(int(num2/2)+1)):
    if num2 % i == 0:
        li2.append(i)
print(li1)
print(li2)

gcd = 0
for ele in li1:
    if ele in li2:
        if ele >= gcd:
            gcd = ele
print(f"GCD of '{num1}' and '{num2}' is {gcd}")