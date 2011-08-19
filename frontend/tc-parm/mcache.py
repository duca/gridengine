#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#       sem título.py
#       
#       Copyright 2011  <edumlopes@Taverna>
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

from google.appengine.api import memcache

class cacher:
	""" Class doc """
	
	def __init__(self,key):
		self.dummy = None
		self.key = key
		self.lista = []
#		if memcache.get(self.key) is None:
#			memcache.add(key,self.lista)
	
	def updatecache(self,data):
		
		memcache.add(self.key,data)

	def update_timed(self, obj, life):
		
		if memcache.replace(self.key,obj,life) is None:
			memcache.add(self.key,obj,life)
			
	def retrieve(self):
		
		return memcache.get(self.key)
		
	def updatelist(self, obj):
		
		data = self.retrieve()
		if data is None:
			l = []
			l.append(obj)
			self.updatecache(l)
		else:
			
			if data.__contains__(obj) is None:
				data.append(obj)
			else:
				self.removeitem(data,obj)
				data.append(obj)
				self.updatecache(data)

	def updatedict(self, key,info,life):

		data = memcache.get(key)
		
		if data is None:			
			memcache.add(key, info,life)
		else:
			memcache.replace(key,info,life)
			
	def retrievedict(self,key):
		
		data = memcache.get(key)
		
		if data is not None:
			return data
		else:
			return -1	
			
	def removeitem(self, data, item):
		
		for i in range(0, len(data)):
			if data[i] == item:
				data.pop(i)
		memcache.replace(self.key, data)
		
def main():
	
	a = []

if __name__ == '__main__':
	main()

