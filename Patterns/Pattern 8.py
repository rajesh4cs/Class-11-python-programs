print("Enter number of rows to see hollow diamond shape.")
print('_'*49)
row = int(input("Enter no.of rows: "))
for i in range((row//2)+1):
 for j in range(1,(row//2+1)-i):
  print(' ', end='')
 for j in range(2*i+1):
  if j==0 or j==2*i:
   print('*',end='')
  else:
   print(' ',end='')
 print()
for a in range(1,row//2+1):
 for b in range(1,a+1):
  print(' ', end='')
 for b in range(row-2*a):
  if b==0 or b==row-2*a-1:
   print('*',end='')
  else:
   print(' ',end='')
 print()
