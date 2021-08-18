'''Write a program that takes a sentence as an input parameter
where each word in the sentence is separated by a space.
The function should replace each blank with a hyphen and 
the return the modified sentence.'''
def hyphen():
    word = input("Enter a string: ")
    j = '-'
    newword = word.replace(' ', '-')
    return newword

b = hyphen() # Calling the function
print(b)