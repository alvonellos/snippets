import sqlite3 as lite
import math

database = './edis.db'

def factorial_lengths(n,db):
	def len_fact(num):
		logsum = 0.0
		for i in xrange(1,num+1):
			logsum += math.log10(float(i))
		if int(num) == 1:
			return int(1)
		else:
			return  int(math.ceil(logsum))

	ssql = """
		CREATE TABLE IF NOT EXISTS factorial_lengths (
			n integer,
			n_length integer,
			UNIQUE(n) ON CONFLICT REPLACE
		)
	"""
	conn = lite.connect(db)
	conn.execute(ssql)
	with conn:
		buff = []
		for i in xrange(1, n+1):
			q = conn.execute("SELECT n from factorial_lengths where n = " + str(i)).fetchone()
			if q is None:
				p = (i, len_fact(i))
				buff.append(p)
		conn.executemany('INSERT INTO factorial_lengths VALUES(?, ?)', buff)
		conn.commit()
	conn.close()
	return "done"
	

if __name__ == "__main__":

	print factorial_lengths(10000, database)
