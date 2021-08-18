# Count the vowels in a string
str = input("Enter a string: ")
count = 0
for vowel in str:
    if vowel in ('a', 'e','i', 'o', 'u'):
        count += 1
print('Number of vowels in the string is',count,end='')
print('.')