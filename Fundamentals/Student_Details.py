#Program to print the details of a student in same line and then in separate lines
name=input("Enter your Name:")
Class=int(input("Enter your class in digits:"))
age=int(input("Enter your age:"))
print("Name:",name,"Class:",Class,"Age:",age)
print("See your details in separate lines")
print("Name:",name,"Class:",Class,"Age:",age,sep='\n')
