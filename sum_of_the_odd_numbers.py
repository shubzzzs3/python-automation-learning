#Sum all odd numbers in a list
num = (input("Please enter the numbers (separated by space): ")).split()
odd = 0
for ele in num:
    if int(ele) % 2 != 0:
        odd = odd + int(ele)
print(f"sum of all odd numbers from list is {odd}")