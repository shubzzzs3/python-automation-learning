#sum of digit
num = input("Enter the num : ")
sum = 0
for i in num:
    sum = sum + int(i)

print(f"The sum of all integers are {sum}")