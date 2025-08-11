#check ig given word is palindrome or not

string = input("Enter the word : ")
if string[0::] == string[::-1]:
    print(f"{string} is palindrome")
else:
    print(f"{string} is not palindrome")

#this code if u dont want to use slicing
"""reversed_str = "" 
for char in string:
    reversed_str = char + reversed_str

if string == reversed_str:
    print(f"{string} is palindrome")
else:
    print(f"{string} is not palindrome")"""


