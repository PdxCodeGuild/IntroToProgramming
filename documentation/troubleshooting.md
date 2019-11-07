# Troubleshooting

Stuck? Want to throw your laptop out the window? Follow the below steps:

## Breathe
Take a deep breath! Don't sweat it. We'll figure this out.

## Read the Error
We tend to associate mistakes with feelings of failure so getting an error in our code can be frustrating. Instead, we should rewire our brains to associate mistakes with **learning**. Every step made (big, small, right, wrong) is one step closer to the solution! So don't beat yourself up and just keep swimming!

```bash
Traceback (most recent call last):
  File ".\random_pie.py", line 30, in <module>
    print(x - y)
TypeError: unsupported operand type(s) for -: 'int' and 'str'
```

Let's read a sample error message.
- First line: HEY! THERE'S AN ERROR.
- Secone line: File name, line number
- Third line: To be clear, let me print the line for you
- Four: Error description.



### Common Errors

#### The term 'xx' is not recognized
Where xx is the typo.

```bash
# command
pu random_pie.py

# error
pu : The term 'pu' is not recognized as the name of a cmdlet,
function, script file, or operable program. Check the spelling
of the name, or if a path was included, verify that the path
is correct and try again.
```

#### No such file or directory
Are you in the right folder? Is the filename spelled correctly? Be sure to include the file extension: ".py"

```bash
# command
py random_pie.py

# error
C:\Program Files (x86)\Python38-32\python.exe: can't open file 'random_pie.py': [Errno 2] No such file or directory

```

#### NameError: name 'xx' is not defined
Where "xx" is the variable/keyword Python does not recognize. Are you trying to use a module? A variable? Did you import? Spelling it correctly?

```bash
Traceback (most recent call last):
  File ".\random_pie.py", line 18, in <module>
    chosen_pie = random.choice(pie_flavors)
NameError: name 'random' is not defined
```

#### unsupported operand type(s) for -: 'int' and 'str'
Are you trying to do math on integers and strings? Convert types! Are you trying to print a number inside a string? Use fstrings!

```bash
Traceback (most recent call last):
  File ".\random_pie.py", line 30, in <module>
    print(x - y)
TypeError: unsupported operand type(s) for -: 'int' and 'str'
```

## Still Stuck?
1. Run your code through [Python Tutor](http://pythontutor.com/visualize.html#mode=edit)
- Python tutor will run your code line by line and show you what's really going on
2. If you're still stuck, ask for help! Try a classmate or a teacher.
