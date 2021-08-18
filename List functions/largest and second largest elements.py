num = int(input("Enter the no. of elements you want in your list: "))
my_list = []
for i in range(num):
    element = int(input("Enter numeric element no.{}: ".format(i+1)))
    my_list.insert(i,element)
print("Your list is",my_list)
n = len(my_list)
for i in  range(n-1):
    for j in range(n-1-i):
        if my_list[j] > my_list[j+1]:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]
print("Largest element:",my_list[n-1])
print("Second largest number:",my_list[n-2])           