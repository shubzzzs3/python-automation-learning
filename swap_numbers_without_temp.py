#Swap two numbers without temp variable
a = int(input("Enter first number :"))
b = int(input("Enter second number : "))
a,b = b,a 
print(a,b)