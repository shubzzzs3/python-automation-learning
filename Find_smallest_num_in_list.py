#Find the smallest number in list
num = list(input("Enter the numbers (please give space after every number) : ").split())
small = int(num[0])
for ele in num:
    if int(ele) <= int(small):
        small = int(ele)
print(small)