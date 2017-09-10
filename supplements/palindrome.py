"""
Write a function that returns True if the input is a palindrome, or False, if it is not.

>>> palindrome('hannah')
True

>>> palindrome('racecar')
True

>>> palindrome('a man, a plan, a canal, Panama')
True

>>> palindrome("1 pound coconut.")
False

>>> palindrome(1234321)
True

"""

def palindrome(word):

    rev = reversed(word)

    if word == word[::-1]:
        return True
    else:
        return False


palindrome('racecar')