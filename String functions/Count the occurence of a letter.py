#Function to count the number of times a character occurs in a string
str = input("Enter a string: ")
ch = input("Enter a character to be searched: ")
c = 0
for a in str:
    if a == ch:
        c +=1

print("Number of times character",ch,"occurs in the string is:",c)
