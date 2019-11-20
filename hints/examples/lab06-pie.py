import random
pie_list = ['apple', 'cherry']
ingredient_list = ['apples', 'cherries']
chosen_pie = input(f"Choose a pie from {pie_list}: ")
in_season = random.choice(ingredient_list)

if in_season == 'apples':
    if chosen_pie == 'apple':
        print('Nice! Apples are in season!')
    if chosen_pie == 'cherry':
        print('Bad time for cherry pie!')

if in_season == 'cherries':
    if chosen_pie == 'apple':
        print('Hmm, maybe wait later for apple pie?')
    if chosen_pie == 'cherry':
        print('Yes! Cherries are on the trees!')
