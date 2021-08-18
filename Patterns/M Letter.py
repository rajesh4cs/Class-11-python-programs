# program to draw "M" letter using loops
for i in range(6):
    for j in range(7):
        if j == 0 or j == 6:
            print('* ',end = '')
        elif (j == i or j == 6-i) and i < 4:
            print('* ',end = '')
        else:
            print('  ',end = '')
    print()