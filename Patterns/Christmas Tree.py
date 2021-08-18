row = int(input("Enter no. of rows: "))
n = row % 4
while n <= row:
    k = 1
    while k <= n:
        print(" " * (row - k), '* ' * k)
        k += 1
    n += 4
k = 0
while k < row:
    print(" " * (row - 5), '* ' * 5)
    k += 1
