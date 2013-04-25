"""
This snippet will take a vertical slice
out of a two dimensional list.
"""
def vslice(list, index):
	for line in list:
		yield line[index]