# <a id="top"></a>Unit 01
[Back to Syllabus](https://github.com/PdxCodeGuild/IntroToProgramming#top)

## Table of Contents
- [Terminal / Command Prompt / Power Shell](#terminal)

### <a id="terminal"></a>Terminal
  | Windows | Mac/Linux | Action |
  | --- | --- | --- |
  | pwd | cd | What is my current directory? |
  | dir | ls | What is in this folder? |
  | cd \<folder_name\> | cd \<folder_name\> | Change directory to \<folder_name\> |
  | cd .. | cd .. | Change directory to parent directory |
  | cls | clear | Clear screen |
  | mkdir \<folder_name\> | mkdir \<folder_name\> | Make directory \<folder_name\> |
  | rmdir \<folder_name\> | rmdir \<folder_name\> | Remove directory \<folder_name\> |
  | py \<file_name\> | python3 \<file_name\> | Run python file in terminal |
  | ctrl + c | ctrl + c | Terminate program |
  | py | python3 | Start python interpreter |
- [Want more?](https://www.w3schools.com/python/python_comments.asp)

### <a id="variables"></a>Variables
- Complete [Exercise 4](https://learnpythonthehardway.org/python3/ex4.html) of Learn Python the Hard Way

### <a id="print"></a>print()  / f-strings
- [Quick overview](https://www.w3schools.com/python/ref_func_print.asp)
- Complete [Exercise 5](https://learnpythonthehardway.org/python3/ex5.html) of Learn Python the Hard Way

### <a id="strings"></a>Datatype: Strings
- [Quick overview](https://www.w3schools.com/python/python_strings.asp)
- Complete [Exercise 6](https://learnpythonthehardway.org/python3/ex6.html) of Learn Python the Hard Way

### <a id="strings"></a>String Concatenation
To concatenate, or combine, two strings you can use the + operator.

Example 1:
```python
a = "Hello"
b = "World"
c = a + b
print(c) # outcome: "HelloWorld"
```

Example 2:
```python
a = "Hello"
b = "World"
c = a + " " + b
print(c) # outcome: "Hello World"
```

### Lab 01: [Hello](https://github.com/PdxCodeGuild/IntroToProgramming/blob/master/labs/lab01-hello.md)

### <a id="input"></a>input()
- [Quick overview](https://www.w3schools.com/python/ref_func_input.asp)

Example 1:
```python
# prints a question to the user
# then allows the user to type an input
# saves user input to a variable
user_name = input("What is your name?") # this line has three actions!

# prints "Hello" with the user's name that they typed in!
print(f"Hello {user_name}!") # outcome: "Hello Lisa"
```

### Lab 02: [Mad Libs](https://github.com/PdxCodeGuild/IntroToProgramming/blob/master/labs/lab02-madlib.md)

[Back to top](#top)
