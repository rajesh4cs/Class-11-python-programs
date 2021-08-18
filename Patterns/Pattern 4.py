'''
PATTERN
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
'''
row=int(input("Enter no. of rows:"))
i = 1
while i <= row:
 a=i
 while a>0:
     print(a,end= ' ')
     a-=1
 i+=1
 print()
