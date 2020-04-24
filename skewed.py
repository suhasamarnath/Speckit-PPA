name = input('Enter the name:')
special =  ['!', '@', '#', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=']
for char in special:
	name = name.replace(char,"")
print(name)	