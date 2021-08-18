#PROGRAM TO DISPLAY A STRING IN REVERSE ORDER
str = input("Enter a string: ")
j = str[-1]
for i in range(-2,-len(str)-1,-1):
    j = j+str[i]
print(j)
if j == str:
    print("String is a palindrome")
else:
    print("String is not a palindrome")