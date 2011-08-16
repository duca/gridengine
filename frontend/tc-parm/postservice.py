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
import datetime
import base64
import simplejson as json
import wsDB

class Tick(messages.Message):
	""" Class doc """

	hostname = messages.StringField(1,required=True)
	load = messages.IntegerField(2,required=True)
	ava_ram = messages.IntegerField(3,required=True)
	kernel = messages.StringField(4,required=True)
	cores = messages.IntegerField(5,required=True)
	key = messages.IntegerField(6,required=True)
	when = messages.IntegerField(7)
	
class TickSuccess(messages.Message):
	
	resp = messages.StringField(1,required=True)

#class Workstation():
#	from Django import simplejson
invdata = "Invalid data"
class ReceiveTick(remote.Service):
	@remote.method(Tick, TickSuccess)
	def regtick(self, request):
		self.request = request
		if request.when:
			when = datetime.datetime.utcfromtimestamp(request.when)
		else:
			when = datetime.datetime.now()
		#summary = self.unfold(self.request.data)
		
		#if summary ==-2:
		#	return TickSuccess(resp="Data is not valid")
#		try:
		host = request.hostname
		regKey = request.key
		carga = request.load
		ava_ram = request.ava_ram
		kern = request.kernel
		nproc = request.cores
#		except:
#			return TickSuccess(resp=request.hostname)
			#return TickSuccess(resp=invdata)
		ticket = wsDB.HeartBeats(hostname=hostname, load=carga, freeram=ava_ram,kernel=kern, nproc = cores, active=True, date=when)	
		try:
			#ticket = wsDB.HeartBeats(host=hostname, carga = load, freeram=ava_ram,kern=kern, nproc = cores, active=True, date=when)
			ticket.put()
		except:
			return TickSuccess(resp="DB unreachable")

		
		return TickSuccess(resp="Data validated")
		
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

