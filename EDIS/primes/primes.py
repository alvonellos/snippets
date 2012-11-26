import sqlite3 as lite

ssql = """
	CREATE TABLE IF NOT EXISTS primes (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		n  INTEGER,
		UNIQUE(n) ON CONFLICT IGNORE
	)"""

isql = r"INSERT INTO primes(n) VALUES(?)"

conn = lite.connect('primes.db')
conn.execute('BEGIN TRANSACTION')
conn.execute(ssql)

def primes():
    current = 1
    while True:
        current += 1
        while True:
            for i in xrange(2, current // 2 + 1):
                if current % i == 0:
                    current += 1
                    break
            else:
                break
        yield current

cur = conn.cursor()
count = 0
comms = 0
for i in primes():
	cur.execute(isql, (i,))
	count = count+1
	if count % 1000 == 0:
		print comms
		count = 0
		comms = comms + 1
		conn.commit()
	
	if comms == 1000:
		conn.commit()
		conn.close()
		exit() 
		
	
