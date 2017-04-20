# Shell Games

Python allows you to execute arbitrary commands via an interactive shell in the terminal. This is a great way to test out a piece of syntax to make sure it does what you want or just to learn new Python commands.

## Objective

Learn how to use Python’s interactive shell to experiment with the language.

1. Open Terminal
1. Type `python` then hit [return]
1. Follow along with your instructor

------

## Hello, world!

The `print` function allows you to output strings to the terminal.

    print('Hello, world!') #> Hello, world!
    print("Hello, world!") #> Hello, world!

------

## Basic Math

Python gives you all of the basic math operators.

    4 + 2  #> 6
    5 - 9  #> -4
    12 / 5  #> 2.4
    4 * 5  #> 20

It also gives you some stranger ones….

Floor division divides then throws away the remainder.

    12 // 5  #> 2

Exponentiation takes a number to a power.

    3 ** 2  #> 9

------

## Imports

Python has available what is called a “standard library”. You can import modules from the standard library and try them out in the shell.

    import math
    math.pi #> 3.141592653589793
    
    import random
    random.choice(['apple', 'pear', 'banana']) #> 'apple'

------

## Exercise

Spend the next few minutes experimenting with Python in the interactive shell. Try some of the examples from this page about the [standard library](https://docs.python.org/3/tutorial/stdlib.html). Interesting ones include `glob`, `re`, `statistics`, `urllib.request`, and `datetime`.
