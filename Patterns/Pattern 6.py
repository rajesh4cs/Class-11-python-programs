'''
PATTERN:
1 2 3 4 5
  1 2 3 4
    1 2 3
      1 2
        1
'''
row = int(input("Enter no. of rows:  "))
a=0
while a < row:
 print(' '*2*a,end='')
 i=1
 while i<row+1-a:
  print(i,end=' ')
  i+=1
 a += 1
 print()
