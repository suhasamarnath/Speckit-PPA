import pprint

def ThreeD(a, b, c):
	lst = [[['x' for row in range(c)]for col in range(b)]for col in range(a)]
	return lst

x = int(input('Enter a value:'))
y = int(input('Enter a value:'))
z = int(input('Enter a value:'))

pprint.pprint(ThreeD(x, y, z))	