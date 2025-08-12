#Count frequency of each character in a string.
string = input("Enter the word:")
for alpha in set(string):
    count = string.count(alpha)
    print(f"{alpha}:{count}")
    