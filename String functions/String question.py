print("\nWelcome to Kids Elementary Technologies")
print('-'*40)
def word():
    str1 = input("Input a sentence: ")
    words = 0
    number_of_characters = len(str1)
    al_num = 0
    str2 = str1.split()
    for a in str2:
        words += 1
    for b in str1:
        if b.isalnum():
            al_num += 1
    print("Original string:", str1)
    print("Number of words are:",words)
    print("Number of characters:",number_of_characters)
    print("Percentage of alphanumeric characters is",(al_num/len(str1))*100,"%")
    print("KEEP LEARNING")
name = input("Enter your name:")
while True:
    if name.isalpha():
        print("Hello,",name,"Now start learning.")
        word()
        break
    else:
        print("Incorrect name.")
        name = input("Enter your name again:")