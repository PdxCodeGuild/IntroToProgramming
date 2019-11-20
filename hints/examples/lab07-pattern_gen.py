import random
pattern_list = ['##', '%%', '//', '~~', '\\\\']
out_pattern = ''
length = 10
for i in range(length):
    out_pattern += random.choice(pattern_list) * 5
    out_pattern += '\n'
print(out_pattern)
