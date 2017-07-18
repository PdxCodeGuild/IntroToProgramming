
# 1) ask the user which units they'd like to use
#     ft, mi, m, km
# 2) ask the user for the number they'd like to convert
# 3) convert the number they entered to meters and display

# 1 ft is 0.3048 m
# 1 mi is 1609.34 m
# 1 m is 1 m
# 1 km is 1000 m

# > what are the units? mi
# > what is the distance? 100
# > 100 mi is 160934 m

units = input('what are the units? ')
distance = input('what is the distance? ')
distance = float(distance)

converted_distance = 0
if units == 'ft':
	converted_distance = distance * 0.3048
elif units == 'mi':
	converted_distance = distance * 1609.34
elif units == 'm':
	converted_distance = distance
elif units == 'km':
	converted_distance = distance * 1000

output = str(distance) + ' ' + units + ' is ' + str(converted_distance) + ' m'
print(output)