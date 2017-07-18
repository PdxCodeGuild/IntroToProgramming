
import random

list_eyes = [':', '=', ';']
list_noses = ['', '-', '\'', '^', '+']
list_mouths = [')', ']', '|', '/', '\\', 'D', 'P', '3']

i = 0
while i < 5:
    eyes = random.choice(list_eyes)
    nose = random.choice(list_noses)
    mouth = random.choice(list_mouths)

    emoticon = eyes + nose + mouth
    print(emoticon)

    i = i + 1
