# BUBBLE SORT
# Ascending order
num = int(input("Enter the no. of elements you want in your list: "))
my_list = []
for i in range(num):
    element = int(input("Enter numeric element no.{}: ".format(i+1)))
    my_list.insert(i,element)
print("Your list is",my_list)
n = len(my_list)
for i in range(n-1):
    for j in range(n-i-1):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
print("Ascending order",my_list)
# Descending order
for i in range(n-1):
    for j in range(n-i-1):
        if my_list[j+1] > my_list[j]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
print("Descending order",my_list)