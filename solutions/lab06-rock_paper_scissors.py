
import random

rps = ['rock', 'paper', 'scissors']

user_choice = input('rock, paper, or scissors? ')
print('user choice: ' + user_choice)

comp_choice = random.choice(rps)
print('computer choice: ' + comp_choice)

# rock - paper
# rock - scissors
# paper - rock
# paper - scissors
# scissors - rock
# scissors - paper

if user_choice == comp_choice:
	print('tie!')
elif user_choice == 'rock' and comp_choice == 'paper':
	print('computer wins!')
elif user_choice == 'rock' and comp_choice == 'scissors':
	print('user wins!')
elif user_choice == 'paper' and comp_choice == 'rock':
	print('user wins!')
elif user_choice == 'paper' and comp_choice == 'scissors':
	print('computer wins!')
elif user_choice == 'scissors' and comp_choice == 'rock':
	print('computer wins!')
elif user_choice == 'scissors' and comp_choice == 'paper':
	print('user wins!')

