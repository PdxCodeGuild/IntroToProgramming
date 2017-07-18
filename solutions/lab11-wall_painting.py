


# 1 gallon can cover 400 sqft of wall

# version 1
# 1) ask the user for the width of the wall
# 2) ask the user for the height of the wall
# 3) calculate the number of gallons of paint needed
# 4) print out the number of gallons

# version 2
# also ask the user for the price-per-gallon
# and calculate the total price of all the paint


wall_width = input('what is the width of the wall? ')
wall_height = input('what is the height of the wall? ')
price_per_gallon = input('what is the price per gallon? $')

wall_width = float(wall_width)
wall_height = float(wall_height)
price_per_gallon = float(price_per_gallon)

wall_area = wall_width * wall_height
gallons = wall_area/400
total_price = gallons * price_per_gallon

print('gallons: ' + str(gallons))
print('total price: $' + str(total_price))

