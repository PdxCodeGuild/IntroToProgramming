favorite_colors = ['orange', 'red', 'yellow']
guesses = []
while len(guesses) < len(favorite_colors):
    one_guess = input("Guess one of my favorite colors: ").lower()
    guesses.append(one_guess)

guesses.sort()
favorite_colors.sort()

if guesses == favorite_colors:
    print("Correct!")

