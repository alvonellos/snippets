from pyalgotrade.tools import yahoofinance
from pyalgotrade.barfeed import yahoofeed
import os

def build_feed(instruments, fromYear, toYear):
	feed = yahoofeed.Feed()
	for year in range(fromYear, toYear+1):
		for symbol in instruments:
			fileName = "%s-%d.csv" % (symbol, year)
			if not os.path.exists(fileName):
				print "Downloading %s %d" % (symbol, year)
				try:
					csv = yahoofinance.get_daily_csv(symbol, year)
					f = open(fileName, "w")
					f.write(csv)
					f.close()
					feed.addBarsFromCSV(symbol, fileName)
				except:
					pass

			
	return feed
	
def build_futures(doprint=True):
	def fix_date(dateStr):
		splitted = dateStr.split('/')
		return splitted[-1] + '-' + splitted[0] + '-' + splitted[1]
		
	import glob
	files = glob.glob('D:/Dropbox/ascii2/*.csv')
	for file in files:
		with open(file, 'r') as input:
			with open(file.split('\\')[-1], 'w') as output:
				output.write('Date,Open,High,Low,Close,Volume,Adj Close\n')
				if doprint: print file
				for line in input:
					splitted = line.split(',')
					buff = fix_date(splitted[2]) + ','
					for x in splitted[3:8]:
						buff += str(x) + ','
					buff += splitted[6]
					output.write(buff + '\n')
					
if __name__ == "__main__":
	build_futures()