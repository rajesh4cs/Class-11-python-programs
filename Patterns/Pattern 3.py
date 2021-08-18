row = int(input())
for i in range(row):
    j = 2*row-1
    for j in range(1,i+1):
        print(' ',end='')
    while j>=1:
        print("* "*j)
        j = j-2
