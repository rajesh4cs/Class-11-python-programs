# Program to find maximum and minimum numbers
n = int(input("Enter first number: "))
max = min = n
for i in range(4):
 n=int(input("Enter next number: "))
 if max<n:
  max=n
 if min>n:
  min=n
print("Maximum=",max)
print("Minimum=",min)
