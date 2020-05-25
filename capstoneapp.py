from capstone import Driver, Employee
ledger = {}
print("-"*30)
print("Welcome to the Shuttle Service")

while True:
	print("_"*30)
	choice = int(input("Select your option:\n\
		\t1. Bus Driver\n\
		\t2. Employee\n"))

	if choice == 1:
		driver_name = input("Name: ")
		driver_phone = int(input("Phone number:"))
		bus_number = input("Bus number: ")
		destination = input("Bus destination: ")
		time = input("Departure time: ")
		seats = int(input("Seats available:"))

		ledger[bus_number] = Driver

	if choice == 2:
		employee_name = input("Name: ")
		employee_phone = int(input("Phone number: "))
		employee_department = input("Department: ")
		department_id = input("Depatment id: ")
		where_to = input("Destination: ")
		seats_booked = int(input("Number of seats to be booked: "))

			

		