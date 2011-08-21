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
from protorpc import messages
from protorpc import remote, message_types
from protorpc.webapp import service_handlers
import datetime,base64
import simplejson as json
import wsDB
import mcache

class Tick(messages.Message):
	""" Class doc """

	hostname = messages.StringField(1,required=True)
	load = messages.IntegerField(2,required=True)
	freeram = messages.IntegerField(3,required=True)
	kernel = messages.StringField(4,required=True)
	cores = messages.IntegerField(5,required=True)
	hostid = messages.IntegerField(6,required=True)
	totalram = messages.IntegerField(7,required=True)
	when = messages.IntegerField(8)
	
class TickSuccess(messages.Message):
	
	resp = messages.StringField(1,required=True)

invdata = "Invalid data"
class ReceiveTick(remote.Service):
	
	@remote.method(Tick, TickSuccess)
	def regtick(self, request):
		machines = wsDB.manager()		
		ticks = mcache.cacher("ticks")
		self.request = request
		if request.when:
			when = datetime.datetime.utcfromtimestamp(request.when)
		else:
			when = datetime.datetime.now()

		try:
			host = request.hostname
			regKey = request.hostid
			carga = request.load
			total = request.totalram
			avaram = request.freeram
			kern = request.kernel
			nproc = request.cores
		except:			
			return TickSuccess(resp=invdata)
		machines.add(host,regKey) #atualiza a lista de hosts
		ticks.updatedict(host,carga,300) #atualiza o dado referente ao computador. Se tiver expirado, insere um novo registro		
		ticket = wsDB.HeartBeats(hostname=host, hostid = regKey, totalram = total, load=carga, freeram=avaram,kernel=kern, cores = nproc, active=1, date=when)	
		try:			
			ticket.put() #efetiva a escrita ao banco
		except:
			return TickSuccess(resp="DB unreachable")

		ans = "Data Validated"
		return TickSuccess(resp=ans)
		
	def unfold(self, data):
		print data
		#splitted = data.split("=")[1]
		try:
			unencrypt = base64.b16decode(data)
		
		except:
			return -2
		decoded = json.dumps(unencrypt)
		return decoded
		
def main():
	
	return 0

if __name__ == '__main__':
	main()

