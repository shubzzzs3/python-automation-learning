# Check count of upparcase letters in string
string = input("Enter the sentesce.")
count = 0
for ele in string:
    if 'A' <= ele <= 'Z':
        count+=1
print(count)
