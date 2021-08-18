#PROGRAM TO DISPLAY A STRING IN REVERSE ORDER
str = input("Enter an string:")
def invert(str):
    inverse = []
    for i in range(-1,-len(str)-1,-1):
        inverse[-i-1] = str[i]
    return inverse
inv = invert(str)
print(inv)
if inv == str:
    print("String is a palindrome")
else:
    print("String is not a palindrome")
