list1 = []
print("How many elements do you want in your list?",end=' ')
n = int(input())
for i in range(n):
    element = int(input("Enter element no. {}: ".format(i+1)))
    list1.append(element)
print("Your list is: ",list1)
for i in list1:
    j = list1.index(i)
    if j == 0:
        list1.append(i)
        del list1[0]
print("List after shifting elements: ",list1)