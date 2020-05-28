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
		while True:

			driver_phone = int(input("Enter Phone number: "))
			if len(str(driver_phone)) == 10:
				if any(obj.driver_phone == driver_phone for obj in Driver.list1):
					print("This phone number is already taken. Enter another one")
				else:
					break
			else:
				print("Enter a valid phone number")

		while True:
			bus_number = input("Bus number: ").replace(" ", "").upper()
			if any(obj.bus_number == bus_number for obj in Driver.list1):
				print("This Bus Number already exists. Enter another number.")
			else:
				break
		
		destination = input("Bus destination: ").upper()
		
		time = input("Departure time: ")
		seats = int(input("Seats available: "))
		Driver.list1.append( Driver(driver_name, driver_phone, bus_number, destination, time, seats))


																		#driver_name, driver_phone, bus_number, destination, time, seats
		ledger[destination] = [bus_number, driver_name]

	if choice == 2:
		employee_name = input("Name: ")
		
		while True:
			employee_phone = int(input("Enter Phone number: "))
			if len(str(employee_phone)) == 10:
				if any(obj.employee_phone == employee_phone for obj in Employee.list2):
					print("This phone number is already taken. Enter another one")
				else:
					break
			else:
				print("Enter a valid phone number")
		
		employee_department = input("Department: ")
		department_id = input("Depatment id: ")
		print("Buses are travelling to the following destinations ( please enter destinations available in the list ): ")
		
		for i in Driver.list1:
			if i.seats == 0:
				continue
			print(i.destination)
		
		while True:
			where_to = input("Enter Destination: ").upper()
			if any(obj.destination == where_to for obj in Driver.list1):
				Employee.list2.append( Employee(employee_name, employee_phone, employee_department, department_id, where_to))
				break
			else:
				print("Enter a valid destination")

		print("Buses travelling in your route: ")
		print("\nDriver Name | Bus No. | Time of Departure | Seats available\n")
  
# print each data item. 
		for obj in Driver.list1:
			if obj.destination == where_to:
				if obj.seats == 0:
					continue
				print(obj.driver_name, obj.bus_number, obj.time, obj.seats, sep = "|")
		while True:
			busno = input("Enter the bus no. that you want to travel in: ").replace(" ","").upper()
			if any(obj.bus_number == busno for obj in Driver.list1):
				break
			else:
				print("Enter a valid Bus Number")


		
		

		



		for obj in Driver.list1:
			if obj.bus_number == busno:
				while True:
					seatsbooked = int(input("Enter the seats you want to book: "))
					if (seatsbooked > obj.seats):
						print("You have booked too many seats. Please enter again.")
					else:
						obj.update(obj.seats, seatsbooked)
						print("Bus details are:")
						print(f"{obj.driver_name}, {obj.driver_phone}, {obj.bus_number}, {obj.destination}, {obj.time}")
						temp = obj
						print("All seats in this bus have now been booked")
						break
				break
		

		print("\nYour seats have been booked!")
		print("\nThe Driver details are:")
		print("\nDriver name: ", temp.driver_name)
		print("Bus number: ", temp.bus_number)
		print("Destination: ", temp.destination)		
		print("Driver phone number: ", temp.driver_phone)
		print("_"*30)
		print("\nYour information:-")
		print("\nName: ",employee_name)
		print("Phone number: ", employee_phone)
		print("Department: ",employee_department)
		print("ID: ",department_id)
		print("Total seats booked: ", seatsbooked)