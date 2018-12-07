# Lab 19: Anagram Checker

Let's write an anagram checker.

## Anagram

Two words are anagrams of each other if the letters of one can be rearranged to fit the other. e.g. `anagram` and `nag a ram`.

Write another function `check_anagram` that takes two strings as parameters and returns True if they're anagrams of eachother, False if they're not. The procedure for comparing the two strings is as follow:

1. Convert each word to lower case (`lower`)
2. Remove all the spaces from each word (`replace`)
3. Sort the letters of each word (`sorted`)
4. Check if the two are equal

```
>>> enter the first word: anagram
>>> enter the second word: nag a ram
>>> 'anagram' and 'nag a ram' are anagrams
```
