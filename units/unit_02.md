# <a id="top"></a> Unit 02

[Back to Syllabus](https://github.com/PdxCodeGuild/IntroToProgramming#top)

## Table of Contents
- [Datatype: Lists](#lists)
- [Modules](#modules)
- [Integers & Operators](#integers)
- [Conditional Statements](conditions)

### <a id="lists"></a>Lists
- [List Overview](https://www.w3schools.com/python/python_lists.asp)
- [List Methods](https://www.w3schools.com/python/python_ref_list.asp)

A list is a collection which is ordered and changeable. In Python lists are written with square brackets.

```python
fruits = [] # empty list
fruits = ["apple", "banana", "cherry"] # initialized list with three items
print(fruits) #outcome: ["apple", "banana", "cherry"]

# print the item at this index position
print(fruits[0]) #outcome: "apple"
print(fruits[1]) #outcome: "banana"
print(fruits[2]) #outcome: "cherry"

# for each item in the fruit list, print the item and its index
for fruit in fruits:
  print(f"{fruit} has an index of {fruits.index(fruit)}")
```

### <a id="modules"></a>Modules
Modules are sources of code; similar to a library. It is a file containing a set of functions you want to include in your application. (For a list of all modules, you can check out the offical [Python docs](https://docs.python.org/3/py-modindex.html)). For this lesson, we will be looking at the [random module](https://pynative.com/python-random-module/). And specifically, we will be looking at the choice() function of the random module: [random.choice()](https://www.w3schools.com/python/ref_random_choice.asp). Please see the example below:

```python
# include the random module in our file
import random

# a list of fruits
fruits = ["apple", "banana", "cherry"]

# randomly choose a fruit and save it to a variable, chosen_fruit
# choice() is a function inside the random module. we use it by writing random.choice()
# the list in which you want the program to choose from, needs to go inside the parenthesis of choice()
chosen_fruit = random.choice(fruits)

# print the value of variable chosen_fruit
print(chosen_fruit)
```
Let's practice random.choice() in the next lab.

### Lab 03: [Magic 8 Ball](https://github.com/PdxCodeGuild/IntroToProgramming/blob/master/labs/lab03-magic_8_ball.md)

---

### <a id="integers"></a>Integers & Operators
- [Integer Overview](https://www.w3schools.com/python/python_numbers.asp)
- [Operators Overview](https://www.w3schools.com/python/python_operators.asp)
- Complete [Exercise 3](https://learnpythonthehardway.org/python3/ex3.html) of Learn Python the Hard Way

### <a id="conditions"></a>Conditional Statements
- [Python Comparison Operators](https://www.w3schools.com/python/python_operators.asp) Scroll down to Comparison Operators
- [Conditional and If statements](https://www.w3schools.com/python/python_conditions.asp)
- Complete [Exercises 1-6](https://www.w3schools.com/python/exercise.asp?filename=exercise_ifelse1) of the PYTHON If...Else section


### Lab 04: [Grading](https://github.com/PdxCodeGuild/IntroToProgramming/blob/master/labs/lab04-grading.md)

### Additional Resources
- Lists, a deep dive
  - [article](https://www.py4e.com/html3/08-lists)
  - [slides](https://www.py4e.com/lectures3/Pythonlearn-08-Lists.pptx)
  - [video](https://www.youtube.com/watch?v=8DvywoWv6fI&t=13722s) (3:48:42 - 4:28:43)
- [Python Module Index](https://docs.python.org/3/py-modindex.html) - all the modules
- Conditional Execution, further explained
  - [article](https://www.py4e.com/lessons/logic)
  - [slides](https://www.py4e.com/lectures3/Pythonlearn-03-Conditional.pptx)
  - [videos](https://www.youtube.com/watch?v=8DvywoWv6fI&t=5160s) (1:26:00 - 1:52:47)

[Back to top](#top)
