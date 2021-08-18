# Program to count words in a line
line = input("Enter a line: ")
x = line.split()
count = 0
for i in x:
    count += 1
print('No. of words in the string is',count)
