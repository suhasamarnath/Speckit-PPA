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
		driver_phone = int(input("Phone number: "))
		bus_number = input("Bus number: ")
		destination = input("Bus destination: ")
		time = input("Departure time: ")
		seats = int(input("Seats available: "))
		Driver.list1.append( Driver(driver_name, driver_phone, bus_number, destination, time, seats))


																		#driver_name, driver_phone, bus_number, destination, time, seats
		ledger[destination] = [bus_number, driver_name]

	if choice == 2:
		employee_name = input("Name: ")
		employee_phone = int(input("Phone number: "))
		employee_department = input("Department: ")
		department_id = input("Depatment id: ")
		where_to = input("Destination: ")
		Employee.list2.append( Employee(employee_name, employee_phone, employee_department, department_id, where_to))

		print("Buses travelling in your route: ")
		print("Driver Name | Bus No. | Time of Departure | Seats available")
  
# print each data item. 
		for obj in Driver.list1:
			if obj.destination == where_to:
				print(obj.driver_name, obj.bus_number, obj.time, obj.seats, sep = "|")

		busno = input("Enter the bus no. that you want to travel in: ").strip()
		seatsbooked = int(input("Enter the seats you want to book: "))

		



		for obj in Driver.list1:
			if obj.bus_number == busno:
				obj.update(obj.seats, seatsbooked)
				print("Bus details are:")
				print(f"{obj.driver_name}, {obj.driver_phone}, {obj.bus_number}, {obj.destination}, {obj.time}")
				temp = obj
				if obj.seats == 0:
					del obj
					print("All seats in this bus have now been booked")
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


		
			

		