num = input("Enter the no. of elements you want in your list: ")
my_list = []
for i in range(num):
    element = input("Enter numeric element no.{}: ".format(i+1))
    my_list.insert(i,element)
count = 0
for i in my_list:
    if len(i) > 1 and i[0] == i[-1]:
        count += 1
print(count)