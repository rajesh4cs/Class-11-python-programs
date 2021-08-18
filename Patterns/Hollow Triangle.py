row = int(input('Enter number of rows required: '))
for i in range(row):
    for j in range(1,row-i):
        print(' ',end='')               # printing space required and staying in same line
    for j in range(2*i+1):
        if i==row-1 and j%2==0:
            print('* ',end='')
        elif j==0 or j==2*i:
            print('*',end='')
        else:
            print(' ',end='')
    print()                             # printing new line
