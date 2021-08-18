# Program: 
# Delete: Odd numbers, negative numbers
# List type: Numeric
num = int(input("Enter the no. of elements you want: "))
my_list = []
for i in range(num):
    element = int(input("Enter numeric element no.{}: ".format(i+1)))
    my_list.insert(i,element)
print("The list is:",my_list)
# Removing odd and negative numbers
len1 = len(my_list)
i = 0
while i < len1:
    if(my_list[i] < 0):
        my_list.pop(i)
        len1 -= 1
        i -= 1
    elif(my_list[i] % 2 != 0):
        my_list.pop(i)
        len1 -= 1
        i -= 1
    i += 1
print("List after deletion :", my_list)
