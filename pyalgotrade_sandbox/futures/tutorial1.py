from pyalgotrade import strategy
from pyalgotrade.barfeed import yahoofeed
from pyalgotrade.technical import ma

from trading_utils import build_feed

class MyStrategy(strategy.Strategy):
    def __init__(self, feed, instrument, smaPeriod):
        strategy.Strategy.__init__(self, feed, 10000)
        self.__sma = ma.SMA(feed[instrument].getCloseDataSeries(), smaPeriod)
        self.__position = None
        self.__instrument = instrument

    def onStart(self):
        print "Initial portfolio value: $%.2f" % self.getBroker().getEquity()

    def onEnterOk(self, position):
        execInfo = position.getEntryOrder().getExecutionInfo()
        print "%s %s: BUY \t at \t $%.2f" % (self.__instrument, execInfo.getDateTime(), execInfo.getPrice())

    def onEnterCanceled(self, position):
        self.__position = None

    def onExitOk(self, position):
        execInfo = position.getExitOrder().getExecutionInfo()
        print "%s %s: SELL \t at \t $%.2f" % (self.__instrument, execInfo.getDateTime(), execInfo.getPrice())
        self.__position = None

    def onExitCanceled(self, position):
        # If the exit was canceled, re-submit it.
        self.exitPosition(self.__position)

    def onBars(self, bars):
        # Wait for enough bars to be available to calculate a SMA.
        if self.__sma[-1] is None:
            return

        bar = bars[self.__instrument]
        # If a position was not opened, check if we should enter a long position.
        if self.__position == None:
            if bar.getClose() > self.__sma[-1]:
                # Enter a buy market order for 10 shares. The order is good till canceled.
                self.__position = self.enterLong(self.__instrument, 10, True)
        # Check if we have to exit the position.
        elif bar.getClose() < self.__sma[-1]:
             self.exitPosition(self.__position)

    def onFinish(self, bars):
        print "Final portfolio value: $%.2f" % self.getBroker().getEquity()

def run_strategy(smaPeriod, instrument, years, future=False):
	if future == False:
		# Load the yahoo feed from the CSV file
		feed = yahoofeed.Feed()
		#feed.addBarsFromCSV("fb", "fb-2013.csv")
		for year in years:
			try:
				build_feed([instrument], year, year)
				feed.addBarsFromCSV(instrument, str(instrument) + "-" + str(year) + ".csv")
			except:
				print "error"
				pass
			
	
		myStrategy = MyStrategy(feed, instrument, smaPeriod)
		myStrategy.run()

	else:
		try:
			feed = yahoofeed.Feed()
			feed.addBarsFromCsv(instrument, str(instrument) + '-' +'057' + '.csv')
			myStrategy = MyStrategy(feed, instrument, smaPeriod)
			myStrategy.run()
		except:
			pass

if __name__ == "__main__":
	instruments = ["orcl", "fb", "aapl"]
	years = [2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013]
	for instrument in instruments:
		run_strategy(60, instrument, years)
		raw_input("Press any key to continue...")
		
	run_strategy(60, 'GC2', '057')