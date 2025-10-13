# Check if a string contains a substring
string = input("Enter the string : ")
sub = input("Enter the substring : ")
if sub in string:
    print("Yes, substring present in string!")
else:
    print("No, substring not present in string!")