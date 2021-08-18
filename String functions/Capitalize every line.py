# Program to capitalize every letter
line = input("Enter a line: ")
length = len(line)
print("Original string is:")
print()
line1 = ""
for a in range(0,length):
    line1 += line[a].capitalize()
print(line1)