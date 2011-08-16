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



class Workstations(db.Model):
	""" Class doc """
	host = db.StringProperty(multiline=False)
	reg = db.IntegerProperty
	active = db.BooleanProperty
	time = db.DateTimeProperty(auto_now_add=True)
	
		
class HeartBeats(db.Model):
	hostname = db.StringProperty(multiline=False)
	reg = db.IntegerProperty
	load = db.IntegerProperty
	freeram = db.IntegerProperty
	totalram = db.IntegerProperty
	kernel = db.StringProperty(multiline=False)
	nproc = db.IntegerProperty
	active = db.BooleanProperty
	date = db.DateTimeProperty(auto_now_add=True)
	#class Tasks(db.Model):
#	taskid = db.IntegerProperty

def main():
	
	return 0

if __name__ == '__main__':
	main()

