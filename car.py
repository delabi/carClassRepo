class Car:
	carCount = 0
	def __init__(self, name="General", model="GM", shapeType="Saloon"):
		self.shapeType = shapeType
		self.name = name
		self.model = model
		self.num_of_doors = 4
		if self.name == "Porshe" :
			self.num_of_doors = 2
		if self.name == "Koenigsegg" :
			self.num_of_doors = 2

		num_of_wheels = 4
		if self.shapeType == "trailer":
			num_of_wheels = 8

		self.speed = 0
		# self.drive = 0
		Car.carCount += 1

	def Car(name="General", model="GM", shapeType="Saloon"):
		car = Car(name, model, shapeType)
		return car

	def drive(self, g):
		self.speed = 11
		return g*self.speed

	def displayCar(self):
		print "Car is: A",self.shapeType, "called ",self.name, self.model

honda = Car('Honda')
print type(honda) is Car
print type(honda)
# Toyota = Car("Sedan", "Toyota", "Corolla")
# Lamborgini = Car("Sports Car","Lamborgini","Reventon")

# Toyota.displayCar()
# Lamborgini.displayCar()
# print "Total Car count: %d" % Car.carCount

