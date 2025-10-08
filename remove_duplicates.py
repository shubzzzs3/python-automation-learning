#remove duplicate elements in a list.
num = input("Enter the num : ").split() #split uses because takinh multi digit input
unique=[]
dup=[]
for i in num:
    if i not in unique:
        unique.append(i)
    

print (num)
print(f"uniques are {unique}")
