# multiplication table
num = int(input("Enter the number : "))
mult = 1
for i in range(1,11):
    mult = num * i
    print (f"{num} * {i} = {mult}")
