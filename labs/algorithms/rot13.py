#!/usr/bin/env python


def shift(char, shift):
    '''
    take a string `char` and get its ASCII integer value 
    and shift it by adding the integer `shift`
    '''
    return ord(char) + shift


def unshift(num, shift):
    '''
    take an integer `num` and subtract the integer `shift`
    from it.  Then turn the integer difference into its
    string ASCII character
    '''
    return chr(num - shift)


def encrypt(message):
    '''
    take a string `message` and iterate it applying the
    `shift` function on each letter and inserting each
    shifted value into `cipher_text`
    '''
    cipher_text = []

    for letter in message:
        cipher_text.append(shift(letter, 13))

    print(cipher_text)
    return cipher_text


def decrypt(cipher):
    '''
    take a list `cipher` and iterate it applying the
    `unshift` function to each list element then string
    concatenate each unshifted element into `message`
    '''
    message = ''

    for letter in cipher:
        message += unshift(letter, 13)

    print(message)
    return message
    

print('--- secret message ---')
secret_message = "attack Pearl Harbor"
print(secret_message)

print('--- encrypted message ---')
encrypted_text = encrypt(secret_message)

print('--- decrypted message ---')
decrypted_text = decrypt(encrypted_text)
