#Program to read three numbers in three variables and swap first two variables with sums of first and second, second and third numbers respectively
a = eval(input("Enter first number: "))
b = eval(input("Enter second number: "))
c = eval(input("Enter third number: "))
print("Number {} and Id of first number: {}:".format(a,id(a)))
print("Number {} and Id of second number: {}:".format(b,id(b)))
print("Number {} and Id of third number: {}:".format(c,id(c)))
print("Sum of the first and second number {} and it's Id: {}".format((a+b),id(a+b)))
print("Sum of the second and third number {} and it's Id: {}".format((b+c),id(b+c)))
x = a+b
y = b+c
d = a
a = x
x = d
d = b
b = y
y = d
print("Number {} and Id of first number: {} after swapping".format(a,id(a)))
print("Sum of the first and second number {} and it's Id: {} after swappping".format(x,id(x)))
print("Number {} and Id of second number: {} after swapping:".format(b,id(b)))
print("Sum of the second and third number {} and it's Id: {} after swapping".format(y,id(y)))
