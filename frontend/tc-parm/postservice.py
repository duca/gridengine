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
from protorpc import service_handlers
import datetime, guestbook
class Tick(messages.Message):
	""" Class doc """
	data = messages.StringField(1, required=True)
	when = messages.IntegerField(2)
	
class TickSuccess(messages.Message):
	
	resp = messages.StringField(1,required=True)

#class Workstation():
#	from Django import simplejson
	
class ReceiveTick(remote.Service):
	@remote.method(Tick, TickSuccess)
	def regtick(self, request):
		self.request = request
		if request.when:
			when = datetime.datetime.utcfromtimestamp(request.when)
		else:
			when = datetime.datetime.now()
			
		note = guestbook.Greeting(content=request.data, date=when)
		note.put()
		return TickSuccess(resp=request.data)

def main():
	
	return 0

if __name__ == '__main__':
	main()

