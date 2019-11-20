user_sleep = input("How much did you sleep last night? ")
user_sleep = int(user_sleep)

if user_sleep < 6:
    print("That's too little!")

if user_sleep > 9:
    print("That's too much!")

if user_sleep >= 6 and user_sleep <= 9:
    print("Nice!")
