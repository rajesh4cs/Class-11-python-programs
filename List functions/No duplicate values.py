num = int(input("Enter the no. of elements you want in your list: "))
my_list = []
for i in range(num):
    element = int(input("Enter numeric element no.{}: ".format(i+1)))
    my_list.insert(i,element)
print("Your list is",my_list)
n = len(my_list)
my_list.reverse()
for i in my_list:
    while my_list.count(i) > 1:
        index = my_list.index(i)
        del my_list[index]
a = my_list.reverse()
print("After removing duplicate elements",a)