# First of all add system path
# import os
# import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

# Method 1:
from TestProject.Decoder import selectName

if __name__ == '__main__':
	print("Hello Main!")


class MyClass():
	def __init__(self):
		print("Hello Class created!")
		selectName.call_architecture()

class Suma():

	def sumando(self,a,b):
		return a+b

# Method 2:
# from TestProject.Decoder.selectName import *
# and call the method as call_architecture(),
# but you don't know from where it is called.
