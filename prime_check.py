#Check if the given number is prime or not

num = int(input("Please enter the number : "))
for i in range(2,num):
    if num % i == 0:
        print(f"{num} is a not prime number")
        print(f"first number {num} is divisible with {i}")
        break
else:
    print(f"{num} is a prime number")
 
    