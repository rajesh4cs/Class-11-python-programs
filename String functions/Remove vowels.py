# Program to remove vowels in a string
string = input("Enter a string: ")
string1 = ''
for i in string:
    if i not in 'aeiouAEIOU':
        string1 = string1 + i
print('Original string is',string1)