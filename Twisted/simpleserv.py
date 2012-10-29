
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.


from twisted.internet import reactor, protocol
import sqlite3 as lite

conn = lite.connect('log.db')
ssql = """
CREATE TABLE IF NOT EXISTS LOG (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip TEXT,
    entry DATE DEFAULT(datetime('now', 'localtime')),
    UNIQUE(ip) on conflict replace)
"""
conn.execute(ssql)
conn.commit()

class Echo(protocol.Protocol):
    """This is just about the simplest possible protocol"""
    def connectionMade(self):
	peer = str(self.transport.getPeer())
	peer = peer[12:len(peer)-1].split(',')[1].replace(' ', '').replace('\'', '')
	conn.execute("INSERT INTO LOG(ip) VALUES(?)", [str(peer)])
	conn.commit()
        print "connection made: " , self.transport.getPeer()           

    def dataReceived(self, data):
        "As soon as any data is received, write it back."
        self.transport.write(data)


def main():
    """This runs the protocol on port 8000"""
    factory = protocol.ServerFactory()
    factory.protocol = Echo
    reactor.listenTCP(51413,factory)
    reactor.run()

# this only runs if the module was *not* imported
if __name__ == '__main__':
    main()
