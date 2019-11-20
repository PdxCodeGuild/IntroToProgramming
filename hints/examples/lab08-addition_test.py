import random
num1 = random.randint(1, 5)
num2 = random.randint(1, 5)
user_answer = input(f"What is {num1} + {num2}? ")
user_answer = int(user_answer)
if user_answer == num1 + num2:
    print("Correct!")
