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

`word ------> "Hello there!"`

Right now we're working with strings and variables. A string starts and end with quotes, and inside you can put a bunch of text that it will have. Python will remember the string as long as a variable is pointing at it.



## Concept: input



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

5 >>> print(f"Here is my message: {my\_variable}")
  Here is my message: Hello there!
```

1. Make the variable `my\_variable` point at everything between the quotes (assign the variable to a string). You can visualize: `my\_variable -----> "Hello there!"

1. When you add two things in quotes, python will just mush them together (concatenate strings). Here, we are mushing together the stuff we see between quotes, `"Here is my message:"`, and the stuff between quotes that `my\_variable` is pointing at.

1. 

Later, we'll let more complex expressions be evaluated within f-strings.

```
>>> print(f"You typed these things: {input(':') + input(':')}")
:ab
:cd
You typed these things: abcd
```
