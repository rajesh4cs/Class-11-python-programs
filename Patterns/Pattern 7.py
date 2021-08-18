'''
PATTERN:
       *
     * * * 
   * * * * * 
     * * *
       *
'''
print("Enter only odd number as input.")
row = int(input("Enter number of rows: "))
i = row-1
j = 1
while i >=0 and j <=row:
 print(' '*i,end='')
 print('* '*j,end='')
 i-=2
 j+=2
 print()
a = 2
b = row-2
while a <=row-1 and b >=1:
 print(' '*a,end='')
 print('* '*b,end='')
 a+=2
 b-=2
 print()
