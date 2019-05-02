# Lab 13: Encode/ROT

Allow the user to choose to enter a letter or a number. If they enter a letter, give them the corresponding number between 1 and 26. If they give a number between 1 and 26, give them the corresponding letter. You can do this using a list of the alphabet, and the `index` method.

## Advanced Version 1

Write a program that prompts the user for a character, and encodes it with ROT13. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

Hint: Keep numbers in the 0 through 25 range using `%`.


| Index   | 0| 1| 2| 3| 4| 5| 6| 7| 8| 9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24|25|
|---------|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
| English | a| b| c| d| e| f| g| h| i| j| k| l| m| n| o| p| q| r| s| t| u| v| w| x| y| z|
| ROT+13  | n| o| p| q| r| s| t| u| v| w| x| y| z| a| b| c| d| e| f| g| h| i| j| k| l| m|


## Advanced Version 2

Let the user type a string, and encode that string. For each character, find the corresponding character, add it to an output string.

## Advanced Version 3

Allow the user to input the amount of rotation used in the encryption / decryption.
