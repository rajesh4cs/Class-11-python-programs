# Leap year program
year = int(input('Enter the year: '))
if year>2021:
 print("Invalid year.")
 print("TRY AGAIN!!!")
elif year%4 ==0:
 print(year,"is a leap year.")
else:
 print(year,"isn't a leap year.")
print("Bye!")
