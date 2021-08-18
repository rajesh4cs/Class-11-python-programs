my_list = []
n = int(input("Enter no. of elements do you want: "))
for i in range(n):
    element = int(input("Enter element no. {}:".format(i+1)))
    my_list.append(element)
print("Your list is",my_list)
p_list = []
n_list = []
for i in my_list:
    if i >= 0:
        p_list.append(i)
    elif i < 0:
        n_list.append(i)
print("Positive numbers list")
print(p_list)
print("Negative numbers list")
print(n_list)    