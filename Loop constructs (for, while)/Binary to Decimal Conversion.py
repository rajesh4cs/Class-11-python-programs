# Program to convert binary into decimal number

n = int(input("Enter a binary number : "))
c = 0
m = 0
while n > 0:
    a = n%10
    b = 2**c
    m += a*b
    c += 1
    n = int(n/10)
print("Your decimal number is :",m)
