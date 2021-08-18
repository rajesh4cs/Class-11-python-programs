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
print("Arranged list is", my_list)
if n%2 == 0:
    print("It has two medians: {}, {}".format(my_list[(n//2)-1], my_list[(n//2)]))
    print("Hence, average of these is considered as median.")
    median = (my_list[(n//2)-1] + my_list[(n//2)])/2
else:
    print("It has only one median.")
    median = my_list[n//2]
print("Median is", median)