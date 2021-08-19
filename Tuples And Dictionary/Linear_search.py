t1 = tuple()
n = int(input("Total no. of values in first tuple: "))
for i in range(n):
	a = input("Enter elements: ")
	t1 += (a,)
n = int(input("Enter the element to be searched :"))
flag = False
for i in range(len(t1)):
    if t1[i] == n:
        print("Element found at index", i)
        flag = True

if flag == True:
    print("Successful search.")
else:
    print("Not found.")