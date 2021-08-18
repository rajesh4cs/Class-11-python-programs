base = int(input("Please Enter the base value :"))
exponent = int(input("Please Enter Exponent Value :"))

power = 1

for i in range(1, exponent + 1):

   power = power * base

print("The Result of {0} raised to the power {1} = {2}".format(base, exponent, power)) 
