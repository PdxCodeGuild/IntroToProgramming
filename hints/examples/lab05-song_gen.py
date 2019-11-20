import random
note_list = ['doh', 're', 'mi', 'fa', 'so', 'la', 'si']
print(random.choice(note_list), random.choice(note_list), random.choice(note_list))

out_song = ''
for num in [1, 2, 3, 4, 5]:
    out_song = out_song + random.choice(note_list) + ' '
print(out_song)
