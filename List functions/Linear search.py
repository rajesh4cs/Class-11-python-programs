# Linear search implementation
num = int(input("Enter the no. of elements you want in your list: "))
my_list = []
for i in range(num):
    element = int(input("Enter numeric element no.{}: ".format(i+1)))
    my_list.insert(i,element)
print("Your list is",my_list)
find = int(input("Enter the element to search: "))
a = 0
for i in my_list:
    if(i == find):
        a = 1
        position = my_list.index(i)
        break
if a == 1:
    print("Element found at index:",position)
else:
    print("Element not found.")