import sqlite3 as lite
import hello
import sys
def getVersion():
	con = None

	try:
		con = lite.connect('test.db')
		cur = con.cursor();
		cur.execute('SELECT SQLITE_VERSION()')

		data = cur.fetchone()

		print "SQLITE version %s" % data

	except lite.Error, e:
		print "Error %s:" %e.args[0]
		sys.exit(1)

	finally:
		if con:
			con.close()

def main():
#	getVersion()
	hello.hello()

if __name__ == '__main__':
	main()
