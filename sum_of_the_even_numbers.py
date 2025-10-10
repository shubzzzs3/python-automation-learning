#Sum all even numbers in a list
num = (input("Please enter the numbers (separated by space): ")).split()
even = 0
for ele in num:
    if int(ele) % 2 == 0:
        even = even + int(ele)
print(f"sum of all even numbers from list is {even}")