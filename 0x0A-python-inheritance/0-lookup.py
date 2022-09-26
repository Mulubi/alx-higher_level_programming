#!/usr/bin/python3

class MyClass1(object):

#Class Attributes
	one = 'first'
	two = 'second'

	''' function that returns the list of available attributes and methods of an object '''

	def __init__(self, my_attr1):
		self.my_attr1 = my_attr1

	def lookup(obj):
		print(self.one, self.two, self.my_attr1)
	
	def my_meth(self):
		pass

m = MyClass1(2)
m.lookup()

#using __dict__ to access attributes of the objects
print(m.__dict__.keys())
