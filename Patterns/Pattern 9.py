row = int(input("Enter no. of rows:"))
for a in range(1,row+1):
 for b in range(1,row+1-a):
  print(' ',end=' ')
 for b in range(a,0,-1):
  print(b,end=' ')
 for b in range(2,a+1):
  print(b,end=' ')
 print()