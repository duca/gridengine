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
from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
import cgi
import datetime
import mcache



class Workstations(db.Model):
	""" Class doc """
	host = db.StringProperty(multiline=False)
	reg = db.IntegerProperty()
	active = db.IntegerProperty()
	time = db.DateTimeProperty(auto_now_add=True)
	
		
class HeartBeats(db.Model):
	hostname = db.StringProperty(multiline=False)
	hostid = db.IntegerProperty()
	load = db.IntegerProperty()
	freeram = db.IntegerProperty()
	totalram = db.IntegerProperty()
	kernel = db.StringProperty(multiline=False)
	cores = db.IntegerProperty()
	active = db.IntegerProperty()
	date = db.DateTimeProperty(auto_now_add=True)
	#class Tasks(db.Model):
#	taskid = db.IntegerProperty

class manager():
	
	def __init__(self):
		
		self.mkey = "wscount"
		self.mname = "machines"
		
	
	def add(self,name, hostid):
		
		res = self.Exist(name,hostid)
		if res is None:
			workstation = Workstations(host=name, reg = hostid, active=1)	
			workstation.put()

		mcount = mcache.cacher(self.mname)
		mcount.updatelist(name)
	
	def retrieve(self):
		mcount = mcache.cacher(self.mname)
		c = mcount.retrieve() #check the cache before fetch results from the database
		if c is None: #if the cache does not hold the info, fetch from db
			query = Workstations.all()
			total = query.count()
			results = query.fetch(total)
		
			if results is not None:
				mcount.updatecache(results) #update cache
				return results
			else:
				results = []
				return results 
		else:
			return c #return cache results otherwise
		
	def retrieveActive(self):
		mcount = mcache.cacher(self.mname)
		c = mcount.retrieve()
		lista = []
		
		if c is None: #cache failure protection. This check up is not well implemented yet
			query = Workstations.all()
			query.filter("active =", 1)
			total = query.count()
			results = query.fetch(total)
			
			if results is not None:
				
				for item in results:
					lista.append(item.host)
				actives = lista
				actives = self.checkActive(results)
				mcount.add(actives) #update cache
				return actives
			else:
				results = []
				return results
		else: 
			return self.checkActive(c)

	def checkActive(self, lista):
		active = []
		mcount = mcache.cacher(self.mname)
		for machine in lista:
			r = mcount.retrievedict(machine)
			if r != -1:
				active.append(machine)
		return active

	def Exist(self,name, hostid):
		
		mdb = Workstations.all()
		mdb.filter("host =", name)
		t = mdb.get()
		
		return t
		
		

def main():
	
	return 0

if __name__ == '__main__':
	main()

