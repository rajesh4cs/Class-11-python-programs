# program to find even and odd number
num = int(input("Enter an number: "))
if num<0:
    print("Please enter positive number.")
elif num%2==0:
    print(num,"is an even number.")
else:
    print(num,"is an odd number.")
