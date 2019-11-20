from string import ascii_lowercase

user_num = input("Give me a number: ")
user_num = int(user_num)
print("Converting to letter...")
print(f"That's letter {ascii_lowercase[user_num-1]}")
