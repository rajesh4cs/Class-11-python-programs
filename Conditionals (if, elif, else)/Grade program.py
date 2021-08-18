# Grade allocation via percentage
pcent = int(input("Enter your percentage: "))
if pcent > 100:
 print('You entered invalid percentage.')
elif pcent < 0:
 print('You entered invalid pecentage.')
elif 0<= pcent < 60:
 print('Your grade is E.')
elif 60 <= pcent < 70:
 print('Your grade is D.')
elif 70 <= pcent < 80:
 print('Yor grade is C.')
elif 80 <= pcent < 90:
 print('Your grade is B.')
else:
 print('Your grade is A.')
