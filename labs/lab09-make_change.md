# Lab 09: Make Change


<div align="center">

## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

## **Stop!**  This syllabus is **deprecated** and has not been updated since April 29, 2020. Intro to Programming has become Programming 101 and Programming 102. Contact your instructor for the link to the correct syllabus. 
***
## !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
</div>


Let the user enter how many pennies they have, and convert their pennies into larger coins and leftover pennies.

## Version 1

Convert the user's pennies into the maximum number of quarters. For example, if the user enters 136, break that 136 into quarters (5) and pennies (11).

## Version 2

Convert the user's pennies into the maximum number of quarters, then the maximum number of dimes, then the maximum number of nickels. Have the user enter the total number in pennies. For example, break 136 into quarters (5), dimes (1), nickles (0) and pennies (1).

## Advanced Version 1

Have the user enter a dollar amount (1.36), convert this to the total in pennies, and proceed as before. Do this with `float()` and `round()`.

## Advanced Version 2

In a while loop, let the user add or subtract a dollar amount to the current coin value, and then convert the resulting value into the smallest number of coins possible.

>\>\>\> You have 5 quarters, 1 dimes, 0 nickles, 1 pennies

>\>\>\> Choose (add), (subtract), or (done) \>subtract

>\>\>\> How much? >.37

>\>\>\> You have 3 quarters, 2 dimes, 0 nickles, 4 pennies

>\>\>\> Choose (add), (subtract), or (done) \>done

## Super Advanced Version 1

Let the user add their own custom coins.

Hint: Use a list and sort

>\>\>\> def get\_index\_two(in\_tuple):

>...		return in\_tuple[2]

>\>\>\> student\_tuples = [

>...     ('john', 'A', 15),

>...     ('jane', 'B', 12),

>...     ('dave', 'B', 10),

>... ]

>\>\>\> sorted(student\_tuples, key=get\_index\_two)   # sort by age

>[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

>\>\>\> sorted(student\_tuples, key=get\_index\_two, reverse=True)   # sort by age, reversed

>[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
