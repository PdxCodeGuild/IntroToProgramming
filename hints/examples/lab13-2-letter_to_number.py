from string import ascii_lowercase

user_let = input("Give me a letter: ").lower()
print("Converting to number...")
print(f"That's number {ascii_lowercase.index(user_let) + 1}")
