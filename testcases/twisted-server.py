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

class Listen(Protocol):
	def connectionMade(self):
		print "Made"
	def dataReceived(self,data):
		#sys.stdout.write(data)
		dado = json.loads(data)
		print dado["nome"]
		print dado["curso"]

def main():
	
	factory = Factory()
	factory.protocol = Listen
	endpoint = TCP4ServerEndpoint(reactor,1090)
	endpoint.listen(factory)
	reactor.run()
	return 0

if __name__ == '__main__':
	main()

