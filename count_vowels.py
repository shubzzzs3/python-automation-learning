#Count the vowels in given string
import math
word = input("Enter the word : ")
vowels = 'aeiouAEIOU'
count = 0
for char in word :
    if char in vowels :
        print(char)
        count+=1
print(count)
        
        

