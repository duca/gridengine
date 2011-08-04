#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#       sem título.py
#       
#       Copyright 2011  <usuario@QNInt>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#       
#       
from twisted.internet.protocol import Factory, Protocol
from twisted.internet import reactor
from twisted.internet.endpoints import TCP4ClientEndpoint
import json

class JSONClient(Protocol):
	#def startedConnecting(self, connector):
		#print "Connecting"
	
	def sendmsg(self):
		
		string = json.dumps({'nome':'eduardo martins', "curso":"eng. fisica"})
		self.transport.write(string)
		print "sent message", string, type(string)
	#def clientConnectionLost(self,connector, reason):
		#print "Lost connection", reason
def gotProtocol(proto):
	proto.sendmsg()
	
def main():
	#reactor.connectTCP("localhost",1079, JSONClientFactory())
	
	factory = Factory()
	factory.protocol = JSONClient
	point = TCP4ClientEndpoint(reactor, "localhost", 1090)
	d = point.connect(factory)
	d.addCallback(gotProtocol)
	reactor.run()
	reactor.stop()
	reactor.run()
	reactor.stop()
	return 0

if __name__ == '__main__':
	main()

