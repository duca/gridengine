#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#       twistedServer.py
#
#       Copyright 2020 Eduardo Martins Lopes <edumlopes@gmail.com>
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
from twisted.internet.endpoints import TCP4ServerEndpoint
import json
import httplib2
class Listen(basic.LineOnlyReceiver):
        """ Protocol definition """
        def connectionMade(self):
                print self.transport.client, "\t Conectou"
                factory.clients.append(client)

        def lineReceived(self,line):
                self.dado = json.loads(line)

                rurl = "http://grid.tecnocientifica.com.br/tick.regtick"
                lurl = "http://localhost:8080/tick.regtick"

                h = httplib2.Http()
                resp, content = h.request(lurl,'POST',line,headers={'Content-Type': 'application/json'})


                print self.dado

        def clientConnectionLost(self):
                factory.clients.remove(client)

class Fact(Listen):
        """ Factory """
        clients = []

        def makeFactory(self):
                factory = Factory()
                factory.protocol = Listen
                return factory

        def start(self):

                factory = self.makeFactory()
                endpoint = TCP4ServerEndpoint(reactor,1080)
                endpoint.listen(factory)
                reactor.run()




def main():

        servidor = Fact()
        servidor.start()

        return 0

if __name__ == '__main__':
        main()
