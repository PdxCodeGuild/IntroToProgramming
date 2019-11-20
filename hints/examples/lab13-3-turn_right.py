from random import randrange
direction_list = ['North', 'East', 'South', 'West']
starting_direction = randrange(4)
print(f"You start out facing {direction_list[starting_direction]}")
right_turns = input("Turn right how many times? ")
new_direction = starting_direction + right_turns
new_direction = new_direction % 4
print(f"You are now facing {new_direction}"
