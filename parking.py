import time
start_time =  time.time()
class Parking:

	two_wheeler_slots = int(input("Enter the number of 2 wheeler slots: "))
	four_wheeler_slots = int(input("Enter the number of 4 wheeler slots: "))

	def __init__(self):
		pass

	def enter(self):
		choice = input("What type of vehicle?\n 1. 2 Wheeler \n 2. 4 Wheeler")	
		if choice == "1":
			self.two_wheeler_slots = self.two_wheeler_slots - 1
			print("Available slots: ", self.two_wheeler_slots)

		elif choice == "2":
			self.four_wheeler_slots = self.four_wheeler_slots - 1
			print("Available slots: ", self.four_wheeler_slots)

	def exit(self):
		type = input("Which vehicle is exiting?\n 1. 2 Wheeler\n 2. 4 Wheeler")	
		if type == "1":
			self.two_wheeler_slots = self.two_wheeler_slots + 1
			print("Available slots:", self.two_wheeler_slots)
			stop_time_2 = (time.time() - start_time)*900
			if stop_time_2 > 3600 and stop_time_2 <= 7200:
				print("Parking fee is ₹10")
			elif stop_time_2 > 7200 and stop_time_2 <= 10800:
				print("Parking fee is ₹20")
			elif stop_time_2 > 10800 and stop_time_2 <=14400:
				print("Parking fee is ₹30")
			else:
				print("Parking fee is ₹50")

		elif type == "2":
				self.four_wheeler_slots = self.four_wheeler_slots + 1
				print("Available slots", self.four_wheeler_slots)
				stop_time_4 = (time.time() - start_time)*900
				if stop_time_4 > 3600 and stop_time_4 <= 7200:
					print("Parking fee is ₹30")	
				elif stop_time_4 > 7200 and stop_time_4 <= 10800:
					print("Parking fee is ₹40")
				elif stop_time_4 > 10800 and stop_time_4 <= 14400:
					print("Parking fee is ₹50")	
				else:
					print("Parking fee is ₹100")

	def available_slots(self):
		print("4 wheeler slots:", self.four_wheeler_slots)
		print("\n 2 wheeler slots: ", self.two_wheeler_slots)

print("Parking Bill")	
while True:
	choice = input("Select: \n 1.vehicle entering \n 2. vehicle exiting \n 3. Available slots")
	if choice == '1':
		vehicle_no = input("Enter the Vehicle number:")
		vehicle = Parking()
		vehicle.enter()
	elif choice == "2":
		vehicle.exit()
		del vehicle
	elif choice == "3":
		vehicle.available_slots()
	else:
		break			




