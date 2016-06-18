class Dog:
	kind = "canine"

	def __init__(self, name):
		self.name = name

d1 = Dog("tommy")
d2 = Dog("doggy")
print "d1 name: %s d1 kind:%s"%(d1.name,d1.kind)
print "d2 name: %s d2 kind:%s"%(d2.name,d2.kind)
