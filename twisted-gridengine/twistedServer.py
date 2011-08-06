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
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory
from twisted.protocols import basic
import sys
from twisted.internet.endpoints import TCP4ServerEndpoint
import json

class Listen(basic.LineOnlyReceiver):
	
	def connectionMade(self):
		print self.transport.client, "\t Conectou"

		
	def lineReceived(self,line):
		dado = json.loads(line)
		print dado["hostname"]
		print dado["load"]
		
class Fact(Listen):

	self.clients = []
	def makeFactory(self):
		factory = Factory()
		factory.protocol = Listen
		return factory
		
	def start(self):
		
		factory = self.makeFactory()
		endpoint = TCP4ServerEndpoint(reactor,1089)
		endpoint.listen(factory)
		reactor.run()
    def clientConnectionMade(self, client):
        self.clients.append(client)

    def clientConnectionLost(self, client):
        self.clients.remove(client)


def main():
	
	servidor = Fact()
	servidor.makeFactory()
	servidor.start()
	
	return 0

if __name__ == '__main__':
	main()

	
