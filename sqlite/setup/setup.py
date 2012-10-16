import sqlite3 as lite
import sys
import glob
import os
import datetime

# This snippet is used as a setup file for
# a program using an sqlite3 database.

def getVersion(database):
	con = None

	try:
		con = lite.connect(database)
		cur = con.cursor()
		cur.execute('SELECT SQLITE_VERSION()')

		data = cur.fetchone()

		return "SQLite version %s" % data
	except lite.Error, e:
		return "Error %s:" % e.args[0]
	finally:
		if con:
			con.close()


def timeStamped(fname, fmt='%Y-%m-%d-%H-%M-%S_{fname}'):
    return datetime.datetime.now().strftime(fmt).format(fname=fname)



def main():
	db = 'trans.db'
	sqlFiles = ['settings.sql', 'init.sql', 'triggers.sql']
	
	print 'This program will make modifications to the database.'
	inputstr = raw_input('Do you wish to continue?[y/n]: ')
	if(inputstr.lower()[0] == 'n'):
		print 'Aborting...'
		sys.exit(0)

	# print getVersion(db)

	
	print 'Initializing ...'
	print 'Using setup file(s) ' + repr(sqlFiles)
	print 'Checking initialization files...'
	if(os.path.isfile(db)):
		print 'Database exists, moving'
		os.rename(db, timeStamped(db))

	exists = dict([(x, os.path.isfile(x)) for x in sqlFiles])
	abort = False
	for (k, v) in exists.iteritems():
		if(v == False):
			print 'Setup file ' + k + ' does not exist.'
			abort = True

	if(abort == True):
		print 'Exiting'
		sys.exit(1)


	for s in sqlFiles:
		execstr = "sqlite3 " + db + " < " + str(s)
		print 'Executing: ' + execstr + '...'
		os.system(execstr)

	print "Done."

if __name__ == '__main__':
	main()
