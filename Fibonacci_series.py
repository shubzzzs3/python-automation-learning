# for fibonacci series
num = int(input("Enter the number : "))
const = 0
new = 1
for i in range(0,num+1):
    print(const, end = " ")
    const, new = new, const+new
    