# Lab 10: Anagram Checker

Let's write an anagram checker.

## Anagram

Two words are anagrams of each other if the letters of one can be rearranged to fit the other. e.g. `dormitory` and `dirtyroom`.

Write a program that lets the user enter two strings, and tells them if they are anagrams of each other.

1. Convert the strings into lists (`list`)
2. Sort the letters of each word (`sort`)
3. Check if the two are equal

```
>>> enter the first word: dormitory
>>> enter the second word: dirtyroom
>>> 'dormitory' and 'dirtyroom' are anagrams
```

# Advanced Version 1

1. Convert each word to lower case (`lower`)
2. Remove all the spaces from each word by replacing them with empty strings (`replace`)

# Advanced Version 2

Make your program ignore punctuation when checking anagrams.

# Advanced Version 3

Let the user enter as many words as they choose. If every word is an anagram of every other word, let the user know.

