#Count lowercase letters in a string
word = input("Please enter the string : ")
count = 0
for ele in word:
    if 'a'<= ele <='z':
        count+=1
print(f"There are {count} lowercase in '{word}'")