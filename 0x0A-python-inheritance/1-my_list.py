#!/usr/bin/python3
""" A class MyList that inherits from list"""


class MyList(list):
	"""implements sorted printing """
	
	def print_sorted(self):
		"""prints the list, but sorted in ascending sort"""
		print(sorted(self))
