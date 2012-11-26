"""
This is a function to step through
a range of numbers by a floating
point increment. 
"""
def drange(x_0, x_1, step):
	curr = float(x_0)
	while curr < x_1:
		yield curr
		curr += float(step)
