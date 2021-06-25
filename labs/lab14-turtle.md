<div align="center">

## *******************************************************

## This syllabus is **deprecated**.

### Intro to Programming has become Programming 101 and Programming 102. 

### **Contact your instructor** for the link to the correct syllabus. 
***
## *******************************************************
</div>

# Lab 1: Turtle

## Explanation

Turtle is a python `module` that allows us to move a virtual turtle around the screen using programming statements. This turtle has a position and a heading.

- `forward(distance)` moves the turtle forward the given number of pixels 
- `left(angle)` and `right(angle)` turns the turtle left or right by the given angle (in degrees)
- `color(color_name)` sets the pen's color, which can be `penup()` `penup()` `penup()`
- `penup()` raises the pen, a line won't be drawn when the turtle moves, `pendown()` lowers the pen again

- `setposition(x, y)` moves the turtle to the given position

- `fillcolor(color_name)` sets the fill color, `begin_fill()` indicates you'd like to begin filling in whatever you draw, `end_fill()` actually fills the shape in.

You can find more commands at https://docs.python.org/3.6/library/turtle.html

## Examples


### Drawing a Square 

```python
from turtle import *

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)

done()

```

### Filling in a Square 

```python
from turtle import *

fillcolor('red')
begin_fill()

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)

end_fill()

done()

```

### Drawing a Star 

```python
from turtle import *

forward(100)
right(144)
forward(100)
right(144)
forward(100)
right(144)
forward(100)
right(144)
forward(100)

done()

```


### Drawing a Square with a Loop

```python
from turtle import *

i = 0
while i < 4:
    forward(100)
    left(90)
    i = i + 1

done()
```

### Drawing a Staircase

```python
from turtle import *

i = 0
while i < 4:    
	forward(100)
	left(90)
	forward(100)
	right(90)
	i = i + 1
done()
```


### Filling in a Square 

```python
from turtle import *

fillcolor('red')
begin_fill()

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)

end_fill()

done()

```

### Draw an N-Sided figure
```python
from turtle import *

edge_length = 1000
n_sides = 5

i = 0
while i < n_sides:
	forward(edge_length/n_sides)
	right(360/n_sides)
	i = i + 1

done()

```


### 8-Sided Spiral

```python
from turtle import *

fillcolor('blue')

n_sides = 8
edge_length = 0

i = 0
begin_fill()
while i < 150:
	forward(edge_length)
	right(360/n_sides)
	i = i + 1
	edge_length = edge_length + 1
end_fill()
done()

```

### Expanding Star

```python
from turtle import *

edge_length = 0
i = 0
while i < 100:
	forward(edge_length)
	right(144)

	edge_length += 4

done()
```

