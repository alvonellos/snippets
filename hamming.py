# Calculate the hamming distance between two strings
def hamdist(str1, str2):
	"""Count the # of differences between strings str1 and str2"""
        diffs = 0
        for ch1, ch2 in zip(str1, str2):
                if ch1 != ch2:
                        diffs += 1
        return diffs

if __name__ == "__main__":
	sr1 = raw_input("Enter str1 (binary): ")
	sr2 = raw_input("Enter str2 (binary): ")
	print hamdist(sr1, sr2)

