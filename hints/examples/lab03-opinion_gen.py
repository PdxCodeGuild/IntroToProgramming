import random
opinion_list = ['excellent', 'good', 'bad', 'horrible']
user_movie = input("What movie do you like? ")
chosen_opinion = random.choice(opinion_list)
print(f"I thought that movie was {chosen_opinion}!")
