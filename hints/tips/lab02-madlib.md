# Lab 2: Mad Libs Tips

## Concept: Strings and Variables

If you try to print a word that's not in quotes, you'll get an error

```
>>> print(word)
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
NameError: name 'word' is not defined
```

This is because `word` isn't pointing at anything. If we put `word` in quotes, it will point at itself

```
>>> print("word")
word
```

We can also use the syntax `word = "other thing"` to make word point at another thing. This will affect `word`, but won't affect `"word"`.

```
>>> word = "Hello there!"
>>> print(word)
Hello there!
>>> print("word")
word
```

You can visualize the variable `word` pointing at the string `"Hello there!"`

`word` -----> `"Hello there!"`

Right now we're working with strings and variables. A string starts and end with quotes, and inside you can put text. Python will remember the string as long as a variable is pointing at it.

```
1 >>> var1 = 'abc'

2 >>> 'def'
  'def'

3 >>> print(var1)
  abc
```

1. Make `var1` point at `abc`: `var1` -----> `'abc'` (assign the variable to the string)

1. Create text in quotes, `'def'`, without a variable pointing at it.

1. We can print out the text in quotes that has a variable pointing at it, so we can print out `'abc'`. We can't print out `'def'` without creating that information again.

## Concept: f-strings

f-strings are strings that let you put variables and other expressions inside of them.

```
1 >>> my\_variable = "Hello there!"

2 >>> print("Here is my message:" + my\_variable)
  Here is my message:Hello there!

3 >>> print("Here is my message: " + my\_variable)
  Here is my message: Hello there!

4 >>> print("Here is my message: {my\_variable}")
  Here is my message: {my\_variable}

5 >>> print(f"Here is my message: {'my\_variable'}")
  Here is my message: my\_variable

6 >>> print(f"Here is my message: {my\_variable}")
  Here is my message: Hello there!
```

1. We make the variable `my\_variable` point at everything between the quotes (assign the variable to a string). You can visualize: `my\_variable -----> "Hello there!"

1. When you add two things in quotes, python will just mush them together (concatenate strings). Here, we are mushing together the stuff we see between quotes, `"Here is my message:"`, and the stuff between quotes that `my\_variable` is pointing at.

1. We add a space at the end of the first string to make the output look nicer.

1. We try to use an f-string. We put the variable in between curly brackets, so that python will know that this section should be seen as referring to other information, and not used as information as itself. Unfortunately, we forget to put an f before the first quote, so python doesn't know that we want an f-string.

5. We make another mistake here. Python will evaluate what's between the curly brackets, but because we put single quotes around `my\_variable`, we are using a string when we mean to use a variable.

6. Here we successfully use the f-string to convey the message.



Later, we'll let more complex expressions be evaluated within f-strings. Here's an example of what f-strings are capable of.

```
>>> print(f"Let me mush together two strings: {'hello' + 'there'}")
Let me mush together two strings: hellothere

>>> nums = [3, 1, 9, 7]
>>> print(f"The maximum number is {max(nums)}")
The maximum number is 9
```

## Concept: input

The easiest structure for understanding input is like this: Ask a question, allow the user to answer, and save the answer as a variable.

```
1 >>> user_color = input("What is your favorite color? ")
2 What is your favorite color? blue

3 >>> print(user_color)
  blue
  >>> print(type(user_color))
  <class 'str'>

```

1. input will print out whatever is in the parentheses, which in this case is `"What is your favorite color? "`. Then the user will type something. When input finishes, it leaves behind whatever the user typed.

2. Here input printed out `"What is your favorite color? "`. After that, the user typed `blue` and pushed enter.

3. Our variable is pointing at `"blue"`, which is a string

Input is much easier to grasp when we are asking questions that make sense. In the next example, let's look at a situation where we use the rules of input in a more arbitrary way. To understand input, we're going to imagine input() disappearing and leaving behind a string version of what the user types

```
1 >>> var1 = 'a' + 'b'
2 >>> var2 = input(':') + 'd'
  :c
  >>> print(var1, var2)
  ab cd
  >>> print('e' + 'f')
  ef
  >>> print('g' + input(':'))
  :h
  gh
```

1. We add `'a'` and `'b'`. With strings, that means they get mushed together (concatenated). You can think of the addition as taking in `'a'` and taking in `'b'`, and then leaving behind `'ab'`. Later, we print out var1, and it prints out `ab`

2. This is similar to line 1, if we just imagine 'c' instead of input. 
