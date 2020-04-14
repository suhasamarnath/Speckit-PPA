details = {}
for x in range(3):
	usn = input("Enter the USN:")
	name = input("Enter the name:")
	details[usn]=name
for key in details:
	print(key,':',details[key])