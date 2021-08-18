# Write a function to count vowel in starting of each word
def VowCount():
    count = 0
    str = input("Enter a string: ")
    word = str.split()
    for i in word:
        if i[0] in 'aeiou' or i[0] in 'AEIOU':
            count += 1
            print(i)
    print("Vowel Words:", count)
VowCount()