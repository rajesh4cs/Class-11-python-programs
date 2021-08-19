t1 = tuple()
n = int(input("Total no. of values in first tuple: "))
for i in range(n):
	a = input("Enter elements: ")
	t1 += (a,)
t2 = tuple()
m = int(input("Total no. of values in second tuple: "))
for i in range(m):
	a = input("Enter elements: ")
	t2 += (a,)
print("First tuple: ",t1)
print("Second tuple: ",t2)
t1, t2= t2, t1
print("After swapping : ")
print("First tuple: ",t1)
print("Second tuple: ",t2)