# Faulty calculator
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
opr = input("Enter the operator for calculation(+,-,*,/,%): ")
if n1==45 and n2==3 and opr=="*":
    print("555")
elif n1==56 and n2==9 and opr=="+":
    print("77")
elif n1==56 and n2==6 and opr=="/":
    print("4")
elif opr=="+":
    n3=n1+n2
    print(n3)
elif opr=="-":
    n3=n1-n2
    print(n3)
elif opr=="*":
    n3=n1*n2
    print(n3)
elif opr=="/":
    n3=n1/n2
    print(n3)
elif opr=="%":
    n3=n1%n2
else:
    print("Error! Please check your input.")