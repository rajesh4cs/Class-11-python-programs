#Pattern:- -5, 10, -15, 20, -25
num = int(input("Enter range: "))
for i in range(1,num+1):
 if i%2 == 0:
  print(5*i,end = ' ')
 else:
  print(-5*i,end = ' ')
