def divide(x, y):
	try:
		result = x // y
		print("Your answer is:",result)
	except ZeroDivisionError:
		print("division by zero")

divide(5, 1)