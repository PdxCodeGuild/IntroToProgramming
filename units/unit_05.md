<div align="center">

## *******************************************************

## This syllabus is **deprecated**.

### Intro to Programming has become Programming 101 and Programming 102. 

### **Contact your instructor** for the link to the correct syllabus. 
***
## *******************************************************
</div>

# <a id="top"></a> Unit 05

[Back to Syllabus](https://github.com/PdxCodeGuild/IntroToProgramming#top)

## Table of Contents
- [Datatype: Dictionaries](#dictionary)
- [Functions](#functions)

## <a id="dictionary"></a>Datatype: dictionaries
- [Overview](https://www.w3schools.com/python/python_dictionaries.asp)
- [Dictionary Methods](https://www.w3schools.com/python/python_ref_dictionary.asp)

Ex:
```python
# The syntax of a dictionary: variable_name = {key: value}

# you can create an empty dictionary
employee_availability = {}

# or initialize a dictionary that contains data

employee_availability = {
"lisa": "Mon", # string
"al": ["Tues", "Wed", "Thurs"], # list
"anthony": ["Mon", "Tues", "Wed", "Thurs", "Fri"] # list
}
# keys: "lisa", "al", "anthony"
# value: "Mon", ["Tues", "Wed", "Thurs"], ["Mon", "Tues", "Wed", "Thurs", "Fri"]

# how many days will Al work in a year?
# 52 weeks in a year multiplied by the number of days worked each week (3)
worked_days = 52 * len(employee_availability["al"])
print(worked_days)

```
Complete [Exercise 1-5](https://www.w3schools.com/python/exercise.asp?filename=exercise_functions1) under PYTHON Dictionaries.

### Lab 12: [Unit Converter](https://github.com/PdxCodeGuild/IntroToProgramming/blob/master/labs/lab12-unit_converter.md)

## <a id="functions"></a>functions
A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

- [Overview](https://www.w3schools.com/python/python_functions.asp)
- Complete [Exercise 1-5](https://www.w3schools.com/python/exercise.asp?filename=exercise_functions1) under PYTHON Functions.

### Additional Resources
Dictionaries, a deep dive
  - [article](https://www.py4e.com/html3/09-dictionaries)
  - [slides](https://www.py4e.com/lectures3/Pythonlearn-09-Dictionaries.pptx)
  - [video](https://youtu.be/8DvywoWv6fI)

[Back to top](#top)
