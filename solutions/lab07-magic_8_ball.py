
# define a list of magic 8 ball responses
# ask the user a question
# randomly choose from your list of responses
# show that answer to the user


# below are some sample answers
'''
It is certain
It is decidedly so
Without a doubt
Yes definitely
You may rely on it
As I see it, yes
Most likely
Outlook good
Yes
Signs point to yes
Reply hazy try again
Ask again later
Better not tell you now
Cannot predict now
Concentrate and ask again
My reply is no
My sources say no
Outlook not so good
Very doubtful
'''

import random

responses = ['Yes', 'No', 'Certainly']
question = input('what is your question? ')
response = random.choice(responses)
print(response)
