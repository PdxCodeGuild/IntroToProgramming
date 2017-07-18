
import random

alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJK@$%#^'

password = ''
i = 0
while i < 20:
	password += random.choice(alphabet)
	i = i + 1
print(password)

