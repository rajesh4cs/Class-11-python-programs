# Insertion sort
# Ascending order
num = int(input("Enter the no. of elements you want in your list: "))
my_list = []
for i in range(num):
    element = int(input("Enter numeric element no.{}: ".format(i+1)))
    my_list.insert(i,element)
print("Your list is",my_list)
for i in my_list:
    j = my_list.index(i)
    while j > 0:
        if my_list[j-1] > my_list[j]:
            my_list[j], my_list[j-1] = my_list[j-1], my_list[j]
        else:
            break
        j -= 1
print("Ascending order", my_list)
# Descending order
for i in my_list:
    j = my_list.index(i)
    while j > 0:
        if my_list[j] > my_list[j-1]:
            my_list[j-1], my_list[j] = my_list[j], my_list[j-1]
        else:
            break
        j -= 1
print("Descending order", my_list)