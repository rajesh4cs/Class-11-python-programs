# Program that adds even numbers in a list upto a definite range set by user
list = []
range = int(input("Enter total number values in a list: "))
i = 1
while i <= range:
    a = int(input("Enter a value: "))
    if a%2 == 0:
        list.append(a)
        i += 1
print("The list of even values(given by you): ",list)