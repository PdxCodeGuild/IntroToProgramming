# Lab: Guess The Number I

###### Delivery Method: Prompt and Demo

--------------

##### Goal

Write a text game in python for a single user to play 'Guess The Number' against
the computer.

--------------------

##### Instructions

Here is how to play 'Guess The Number':

1. Display a welcome screen to the user.
1. The Computer chooses a random number between 1 and 2 billion.
1. After the computer chooses a number, the human attempts to guess the computer's secret number in as few guesses as possible. The human:

    - Guessses a number
    - The computer will respond with a message 'too high!' or 'too low!'
    - Repeat until the human guesses the exact number correctly.


1. score is kept like golf: lower is better!


-------------------

#### Documentation

1. [Python Official: random.randint()](
https://docs.python.org/3/library/random.html)

1. [Python Official: Control Flow Tools](
https://docs.python.org/3/tutorial/controlflow.html)

1. [Python Official: time.sleep()](
https://docs.python.org/3/library/time.html#time.sleep)


-----------------------
#### Advanced

- Use `time.sleep()` to make the computer _think_, and pause momentarily.
- Ask for different difficulty levels by adjusting the maximum number.
- Play multiple rounds, prompting to 'play again?'.


----------------------

#### Key Concepts

- Random Module
- Flow Control
- Event Loop Pattern
- PEP8
