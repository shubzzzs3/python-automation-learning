#Check if two strings are anagrams
first = input("Enter first word :").lower()
second = input("Enter second word :").lower()
if sorted(first) == sorted(second):
    print(" both are anagrams")
else:
    print("both are not anagrams")