
# 1) ask the user for the number grade (e.g. 86)
# 2) find the number grade associated with that letter grade
# 	e.g. if grade is greater than 90, show the user 'A'


user_grade = input('what is your number grade? ')
user_grade = int(user_grade)


if user_grade >= 90:
	print('A')
elif user_grade >= 80:
	print('B')
elif user_grade >= 70:
	print('C')
elif user_grade >= 60:
	print('D')
else:
	print('F')



# the longer way
'''
if user_grade >= 90:
	print('A')

if user_grade < 90 and user_grade >= 80:
	print('B')

if user_grade < 80 and user_grade >= 70:
	print('C')

if user_grade < 70 and user_grade >= 60:
	print('D')

if user_grade < 60
	print('F')
'''

	
