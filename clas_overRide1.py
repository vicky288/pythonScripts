class Parent:
	def __init__(self,val):
		self.value = val

	def getVal(self):
		return self.value


class Child(Parent):
	def getVal(self):
		return self.value + 1


p1 = Parent(1)
c1 = Child(1)

print "p1:%d \nc1:%d\n"%(p1.getVal(),c1.getVal())
