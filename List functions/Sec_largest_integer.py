# Program to find second largst integer using append function in list
n = int(input("Enter the number of elements in the list: "))
list = []
i = 0
while i < n:
    num = int(input("Enter list values: "))
    list.append(num)
    i += 1
print("The original list is: ",list)
if list[0] > list[1]:
    m1, m2 = list[0], list[1]
else:
    m1, m2 = list[1], list[0]
for x in list[2:]:
    if x > m2:
        if x > m1:
            m1, m2 = x, m1
        else:
            m2 = x
print()
print("The second largest element in the list is:",m2)