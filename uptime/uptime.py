from socket import *
import sqlite3 as lite
import subprocess
import sys
import os
import time
"""
  Uptime script to monitor Dr. Whitaker's computers 
  in the mountain.
"""
def db_name():
	s = gethostname().replace('.', '').strip('\'').lower()
	return s + '_uptime.db'

 
def test_port(ip_address, port, timeout=3): 
    s = socket(AF_INET, SOCK_STREAM) 
    s.settimeout(timeout) 
    result = s.connect_ex((ip_address, port)) 
    s.close() 
    if(result == 0): 
        return True 
    else: 
		return False

def test_all(host_list, port):
	for host in host_list: 
		if test_port(gethostbyname(host), port): 
			print 'Successfully connected to ', 
		else: 
			print 'Failed to connect to ', 
		print '%s on port %d' % (host, port)
		
def main():
	host_list = ['www.google.com', '192.168.1.1']
	port = 80


	ssql = "CREATE TABLE IF NOT EXISTS LOG (ID INTEGER PRIMARY KEY AUTOINCREMENT,\
			ENTRYDATE DATETIME, ROUTER TEXT, GOOGLE TEXT)"
	trig = """
	CREATE TRIGGER IF NOT EXISTS update_datetime AFTER INSERT ON LOG
	BEGIN
		UPDATE LOG SET ENTRYDATE = DATETIME('NOW') WHERE rowid = new.rowid;
	END;
	"""
	conn = lite.connect(db_name())
	conn.execute(ssql)
	conn.execute(trig)
	cur = conn.cursor()
	try:
		while True:
			try:
				router = str(test_port(gethostbyname(host_list[1]), port))
				google = str(test_port(gethostbyname(host_list[0]), port))
				cur.executemany("INSERT INTO LOG (ROUTER, GOOGLE) VALUES(?,?)", zip([router], [google]))		
				print zip([router], [google])
				time.sleep(10)
				conn.commit()
			except Exception:
				print 'caught exception'
				cur.executemany("INSERT INTO LOG (ROUTER, GOOGLE) VALUES(?,?)", zip(['exception'], ['exception']))		
				
	except KeyboardInterrupt:
		print 'Interrupt caught, terminating'
		conn.commit()
		conn.close()
		quit()


if __name__ == "__main__":
	main()


