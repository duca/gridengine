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
import httplib2
import data
import json


def main():

	f = data.Fetcher(2,3)
	
	s = f.fetch()
	
	enc = json.dumps(s)
	
	lurl = "http://localhost:8080/tick.regtick"
	rurl = "http://grid.tecnocientifica.com.br/tick.regtick"
	furl = "http://200.136.224.204:8091/tick.regtick"	
	h = httplib2.Http()
	resp, content = h.request(lurl,'POST',enc,headers={'Content-Type': 'application/json'})
	print resp
	print content

	
	return 0

if __name__ == '__main__':
	main()

