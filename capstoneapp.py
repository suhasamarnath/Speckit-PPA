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

		ledger[destination] = [bus_number, driver_name]

	if choice == 2:
		employee_name = input("Name: ")
		employee_phone = int(input("Phone number: "))
		employee_department = input("Department: ")
		department_id = input("Depatment id: ")
		where_to = input("Destination: ")

	print("View buses in my route: ")
	print ("{:<10} {:<10} {:<10}".format('DESTINATION', 'BUS NO.', 'DRIVER')) 
  
# print each data item. 
	for key, value in ledger.items(): 
    	destination, bus_number, driver_name = value 
   		print ("{:<10} {:<10} {:<10}".format(destination, bus_number, driver_name))	
		
			

		
