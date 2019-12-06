## <a id="top"></a>Unit 03
[Back to Syllabus](https://github.com/PdxCodeGuild/IntroToProgramming#top)

## Table of Contents
- [while loop](#while)
- [break](#break)
- [else](#else)
- [for x in range()](#range)
- [for each](#each)
- [continue](#continue)
- [for x in range](#range)

Today, we'll warm up with a lab first.

### Lab 05: [Emoticon](https://github.com/PdxCodeGuild/IntroToProgramming/blob/master/labs/lab05-emoticon.md)
Do the simple one first. Go back and try the advance ones after we learn about loops.
(Hint: [concatenating](https://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python))

### Loops

#### while <a id="while"></a>loop
Do something while statement is true.

```python
i = 1 # set variable i equal to the value of 1
while i < 6: # as long as i (1) is less than 6, run the following
  print(i) # print i (1 on the first round)
  i += 1 # after printing i (1), add 1 to i (1). i is now 2
```

Complete [Exercise 1](https://www.w3schools.com/python/exercise.asp?filename=exercise_loops1) of PYTHON Loops.

#### <a id="break"></a>break

The break keyword is used to break out a for loop, or a while loop.

```python
i = 1 # set variable i equal to the value of 1
while i < 6: # as long as i (1) is less than 6, run the following
  print(i) # print i (1 on the first round)
  if i == 3: # on every loop, check if i == 3
    break # if it does, exit the while loop and stop counting
  i += 1 # after printing i (1), add 1 to i (1). i is now 2
```

#### <a id="else"></a>else
Do something while statement is true. When it is no longer true, do something else.

Complete [Exercise 2](https://www.w3schools.com/python/exercise.asp?filename=exercise_loops2) of PYTHON Loops.

```python
i = 1 # set variable i equal to the value of 1
while i < 6: # as long as i (1) is less than 6, run the following
  print(i) # print i (1 on the first round)
  i += 1 # after printing i (1), add 1 to i (1). i is now 2
else: # the moment, i is 6, the while statement goes from True to False
  print("i is no longer less than 6") # this will now print
```

Complete [Exercise 3](https://www.w3schools.com/python/exercise.asp?filename=exercise_loops3) of PYTHON Loops.

#### <a id="continue"></a>continue

```python
# Skip the iteration if the variable i is 3, but continue with the next iteration:
for i in range(9):
  if i == 3:
    continue
  print(i)
```
Complete [Exercise 4](https://www.w3schools.com/python/exercise.asp?filename=exercise_loops4) of PYTHON Loops.

#### <a id="range"></a>for x in range()

Do something for a set number of times.

```python
# x here is just a placeholder. it will do the counting for us
for x in range(3): # do the following 3 times
  print("Hello!")

# outcome: each item of the list on a new line
"Al"
"Anthony"
"Lisa"
```

Complete [Exercise 5](https://www.w3schools.com/python/exercise.asp?filename=exercise_loops1) of PYTHON Loops.

#### <a id="each"></a>for each

Do something to each item in a list.

```python
# initialize a list with student names and save to a variable, students
students = ["Al", "Anthony", "Lisa"]
# the student variable only exists in this for loop. you cannot use "student" anywhere else
# studentS is the list variable we created a bove
for student in students: # for each item in the list, do this:
  print(student)
```

### Lab 06: [Rock Paper Scissors](https://github.com/PdxCodeGuild/IntroToProgramming/blob/master/labs/lab06-rock_paper_scissors.md)
You don't need loops to complete the lab. BUT you will need them for the advance versions. Give it a shot and try to incorporate loops into your code.

**Additional Resources**
- Loops & Iteration
  - [article](https://www.py4e.com/html3/05-iterations)
  - [slides](https://www.py4e.com/lectures3/Pythonlearn-05-Iterations.pptx)
  - [video](https://www.youtube.com/watch?v=8DvywoWv6fI&t=8121s) (2:15:21 - 2:58:38)

[Back to top](#top)
