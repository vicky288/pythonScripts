class Calculator:
	def __init__(self, ina, inb):
		self.a = ina
		self.b = inb

	def add(self):
		return self.a + self.b

	def mul(self):
		return self.a * self.b


newCalculation = Calculator(10,20)
print "Add Val:%d"%newCalculation.add()
print "Mul Val:%d"%newCalculation.mul()
