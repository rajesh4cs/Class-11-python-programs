print("Enter numbers separated by comma :")
t1 = tuple([int(e) for e in input().split(',')])
i = 0
print('-'*12)
for e in t1:
    if i == t1.index(e):
        print('|',e, ' - ', t1.count(e),'|')
    i += 1
print('-'*12)