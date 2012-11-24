import os, fnmatch, sys

def usage():
	usagestr = "usage: python " + sys.argv[0] + """
		<path> <filter> [-v]
	""" + '\n ex: python ' + sys.argv[0] + " / *.py "
	print usagestr

def print_matches(rootPath, pattern, verbose=True):
	file_count = 0
	line_count = 0
	for root, dirs, files in os.walk(rootPath):
		for filename in fnmatch.filter(files, pattern):
			file_count += 1
			file_line_count = 0
			infile = os.path.join(root, filename)
			with open(infile) as f:
				for line in f:
					file_line_count += 1
			if verbose:
				print infile + " | " + str(file_line_count)
			line_count += file_line_count

	return {"file_count: " : file_count, "line_count: " : line_count}
				
def main():
	file_count = 0
	line_count = 0
	verbose = False
	if len(sys.argv) > 3:
		if sys.argv[3] == '-v':
			verbose = True
	
	print print_matches(sys.argv[1], sys.argv[2], verbose)

if __name__ == "__main__":
	if len(sys.argv) == 1:
		usage()
	else:
		main()

