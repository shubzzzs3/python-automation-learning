#Find LCM of two numbers
num1 = int(input("please enter the first number : "))
num2 = int(input("please enter the second number : "))
li1 = []
li2 = []
a = 0
b = 0
for i in range(1,100):
    a= num1 * i
    li1.append(a)

for i in range(1,100):
    b= num2 * i
    li2.append(b)
lcm = 0
for ele in li1:
    if ele in li2:
            lcm = ele
            break
print(f"LCM for '{num1}' and '{num2}' is {lcm}")           
    
