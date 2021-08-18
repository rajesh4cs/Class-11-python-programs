# Driving age program
age = int(input("What is your age? "))
if 100>=age>18:
    print("You can drive.")
    print("Drive carefully!!!")
elif age==18:
    print("I can't decide. Please ask at vehicle licensing office.")
elif age>100:
    print("You seem to be too old. Please enter your correct age. It is not a valid age.")
elif 0<age<7:
    print("You are a baby child. Pls do not think about riding motor vehicle.")
elif 7<=age<18:
    print("You can't drive.")
elif age<=0:
    print("You don't exist.")