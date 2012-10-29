import sqlite3 as lite
import operator
import socket
import cPickle

def get_hostname(ipaddr):
	try:
		triplet_set = socket.gethostbyaddr(ipaddr)
	except:
		triplet_set = socket.gethostbyaddr('127.0.0.1')
	table = []
	table.append([str(ipaddr), str(triplet_set), str(triplet_set[0]), str(triplet_set[1]), str(triplet_set[2])])
	reduced = reduce(operator.add, table)
        reduced[-1] = reduced[-1].replace("]", '').replace("[", '').replace('\'', '')
        reduced[-2] = reduced[-2].replace("]", '').replace("[", '').replace('\'', '')
	return reduced

if __name__ == "__main__":
	ssql = r"""
	CREATE TABLE IF NOT EXISTS RESOLVED (
	    id INTEGER PRIMARY KEY AUTOINCREMENT,
	    raw_input TEXT,
	    raw_output TEXT,
	    hostname TEXT,
	    aliaslist TEXT,
	    ipaddrlist TEXT
        )
	"""
	
	conn = lite.connect('log.db')
	buf = []
	with conn:
		cur = conn.cursor()
		cur.execute('SELECT ip from LOG')
		row = cur.fetchone()
		while row != None:
			ip = str(row[0])
			buf.append(get_hostname(ip))	
			row = cur.fetchone()
		print buf
		cPickle.dump(buf, open('buf.p', 'wb'))
		raw_input("Press any key to continue")
		conn.execute(ssql)
		cur.executemany("INSERT INTO RESOLVED (raw_input, raw_output, hostname, aliaslist, ipaddrlist) VALUES(?,?,?,?,?)", buf)

					
