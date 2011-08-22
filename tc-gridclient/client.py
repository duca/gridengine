#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#       sem título.py
#       
#       Copyright 2011 Eduardo Martins Lopes <eduardo@Motorhome>
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

import data, erros, sys, time, httplib2, json

class cliente:
	
	def __init__(self,key):
		
		
		lurl = "http://localhost:8080/tick.regtick"
		rurl = "http://grid.tecnocientifica.com.br/tick.regtick"
		furl = "http://200.136.224.204:8091/tick.regtick"	
		self.url = rurl
		self.errors = erros.logger("cliente_erros.log");
		self.errors.calee = "cliente.py";
		
		self.fetcher = data.Fetcher(1,key);
		self.datalogger = True
	
	def work(self, timer):
		import time;	
		try:
			pidf = open(".client.pid","r")
			pid = True
			pidf.close()
		except:
			pidf = open(".client.pid","w")
			pidf.close()
			pid = True
			
		while pid:
			
			string = self.fetcher.fetch();
			enc = json.dumps(string)
			h = httplib2.Http()
			try:
				resp, content = h.request(self.url,'POST',enc,headers={'Content-Type': 'application/json'})		
				print "Tick"
			except:
				error = "Couldnt connect to %s" & (str(self.url))
				self.datalogger.reg(error,1)
				print "Failed"
			#checagem de existencia de arquivo
			try:
				pidf = open(".client.pid","r")
				pid = True
				pidf.close()
			except:
				pid = False
				self.errors.reg("Interrompido", 0)
			time.sleep(timer)
			

	def datalog(self):
		from time import sleep
		
		while self.datalogger:
			
			#self.data_sum = self.fetcher.update_data();
			#self.con.root.reg_workstation(self.data_sum)
			sleep(300);
			f = data.Fetcher(2,key)
	
	
	
		
		
		

if __name__ == '__main__':
	
	from multiprocessing import Process
	import random
	
	r = random.Random()
	
	
	try:
		f = open(".key.dat", "r")
		key = str(f.read())
		
		if len(key) == 0:
			key = r.randint(1,1000000)	
			f = open(".key.dat", "w")
			f.write(key)
		else:
			key = int(key)
	except:
		key = r.randint(1,1000000)
		f = open(".key.dat", "w")
		f.write(str(key))	
	client = cliente(key);

	fetch_thread = Process(target=client.work, args=(300,))
	fetch_thread.start()
	
	

