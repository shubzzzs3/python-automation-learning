#Sum of squares of first N numbers
num = int (input("Enter the number till you eant sum :"))
total = 0
for i in range(1,num+1):
    total = total + (i**2)
print(f"Sum of squares of first {num} numbers is: {total}")