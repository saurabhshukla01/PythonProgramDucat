# colourser  nonlocal  value form of using def mathod in python ....????


a=0
def Sample():
	a=25
	def example():
		nonlocal a
		a=50
		print("In Sample",a)
	example()
	print("In example",a)
Sample()
print("In main",a)


"""
output ==

In Sample 50
In example 50
In main 0

"""