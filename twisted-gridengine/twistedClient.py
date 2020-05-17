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
from twisted.protocols import basic
from twisted.internet import reactor,task
from twisted.internet.endpoints import TCP4ClientEndpoint
import json
import data
import base64, urllib, urllib2

rhost = "localhost:8080/tick.regtick"
class JSONClient(basic.LineOnlyReceiver):
	#def startedConnecting(self, connector):
		#print "Connecting"
	
	def sendmsg(self):
		from time import sleep
		workstation = data.Fetcher(2)
		ws_data = workstation.fetch()	
		self.string = json.dumps(ws_data)
		self.sendLine(self.string)		
		encrypted = base64.b16encode(self.string)
		mala = urllib.urlencode({'data': encrypted})
		try:
			f = urllib2.urlopen(rhost, mala)
		except:			
			f = []
			print "Connection failed"



class Con(Protocol):
	""" Class doc """
	
	def __init__ (self):
		""" Class initialiser """
		self.lc = task.LoopingCall(self.tick)
		#pass
	def makeFactory(self):
		self.factory = Factory()
		self.factory.protocol = JSONClient
		return self.factory
	
	def gotProto(self, proto):
		self.proto = proto
		
		self.lc.start(2)
		
	def tick(self):
		self.proto.sendmsg()

	def connect(self):
		
		factory=self.makeFactory()
		point = TCP4ClientEndpoint(reactor, "localhost", 1080)
		d = point.connect(factory)
		d.addCallback(self.gotProto)
		reactor.run()
	
def main():
	#reactor.connectTCP("localhost",1079, JSONClientFactory())
	
	cliente = Con()
	
	cliente.connect()
	return 0

if __name__ == '__main__':
	main()

