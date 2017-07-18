
str_adj = input('give me an adjective: ')
str_noun = input('give me a noun: ')
str_animal = input('give me an animal: ')
str_noise = input('give me a noise: ')

output =  f'{str_adj} Macdonald had a {str_noun}, E-I-E-I-O\n'
output += f'and on that {str_noun} he had an {str_animal}, E-I-E-I-O\n'
output += f'with a {str_noise} {str_noise} here\n'
output += f'and a {str_noise} {str_noise} there,\n'
output += f'here a {str_noise}, there a {str_noise},\n'
output += f'everywhere a {str_noise} {str_noise},\n'
output += f'{str_adj} Macdonald had a {str_noun}, E-I-E-I-O.\n'

print(output)