#reverse the string without using slicing or reverse
string = input("Enter the word")
reversed_str = " "
for char in string:
    reversed_str = char + reversed_str
print(reversed_str)