# Program to calculate sum of digits present in a string
a = input("Enter a string with digit: ")
b = 0
for i in a:
    if i.isdigit():
        b += int(i)
print("Sum of digits in the string:",b)