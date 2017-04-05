class Car(object):

	speed = 0

	def __init__(self, name="General", model="GM", shapeType="saloon"):
		self.shapeType = shapeType
		self.name = name
		self.model = model
		self.num_of_doors = 4
		self.num_of_wheels = 4
		self.speed = 0

		if self.name == "Porshe" :
			self.num_of_doors = 2
		if self.name == "Koenigsegg" :
			self.num_of_doors = 2
		
		if self.shapeType == "trailer":
			self.num_of_wheels = 8

		

	def Car(name="General", model="GM", shapeType="saloon"):
		car = Car(name="General", model="GM", shapeType="saloon")
		return car

	def is_saloon(self):
		if self.shapeType != "trailer":
			return True

	# @classmethod
	def drive(self, g):
		if g == 7:
			self.speed = 77
		if g == 3:
			self.speed = 1000
		return self

	# def displayCar(self):
	# 	print "Car is: A",self.shapeType, "called ",self.name, self.model

# class Car(Car):

# 	def __init__(self, name="General", model="GM", shapeType="saloon"):
# 		# Car.__init__(self, name="General", model="GM", shapeType="saloon")

# 		self.speed=0

# 		def drive(self, g):
# 			if g == 7:
# 				self.speed = 77
# 				return self.speed

	

man = Car('MAN', 'Truck', 'trailer')
parked_speed = man.speed
ka_speed = man.drive(7)
moving_speed = man.drive(7).speed

# print "Parked Speed: ",parked_speed
# print "Ka Speed: ", ka_speed

# honda = Car('Honda')
# print type(honda) is Car
# print type(honda)
# Toyota = Car("Sedan", "Toyota", "Corolla")
# Lamborgini = Car("Sports Car","Lamborgini","Reventon")

# Toyota.displayCar()
# Lamborgini.displayCar()
# print "Total Car count: %d" % Car.carCount

