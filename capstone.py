class Driver:
	def __init__(self, driver_name, driver_phone, bus_number, destination, time, seats):
		self.driver_name = driver_name
		self.driver_phone = driver_phone
		self.bus_number = bus_number
		self.destination = destination
		self.time = time
		self.seats = seats

	def update(self, seats_booked):
			seats = seats - seats_booked

	#def booked(self, ):
				

class Employee:
	def __init__(self, employee_name, employee_phone, employee_department, department_id, where_to, seats_booked):
		self.employee_name = employee_name
		self.employee_phone = employee_phone
		self.employee_department = employee_department
		self.department_id = department_id
		self.where_to = where_to		
		self.seats_booked = seats_booked
