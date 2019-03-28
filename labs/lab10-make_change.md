
# Lab 10: Make Change

Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first, resulting in the fewest amount of coins. For this, you'll have to use floor division `//`, which throws away the remainder. `10/3` is `3.333333`, `10//3` is `3`.

## Version 1

Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136. Then break that 136 into quarters (5) and pennies (11).

## Version 2

Have the user enter the total number in pennies, e.g. for $1.36, the user will enter 136. Then break that 136 into quarters (5), dimes (1), nickles (0) and pennies (1).

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
