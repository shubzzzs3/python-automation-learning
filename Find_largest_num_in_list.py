#FInd the largest number in list
num = list(input("Enter the numbers (please give space after every number) : ").split())
large = int(num[0])
for ele in num:
    if int(ele) >= int(large):
        large = int(ele)
print(large)