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



class cliente:
	
	def __init__(self, mach, porta):
		import rpyc, data, erros, sys, time
		

		errors = erros.logger("cliente_erros.log");
		errors.calee = "cliente.py";
		try:
			self.con = rpyc.connect(mach,port=porta);
			self.bgsrv = rpyc.BgServingThread(self.con)
		except:
			errors.reg("Server not available, check connection", 3)
			sys.exit();
		self.fetcher = data.Fetcher(1);
		self.fetcher.work_start();
		self.datalogger = True
	
	def fetch_work(self, timer):
		import time;	
		while len(self.fetcher.summary) == 0:
			time.sleep(timer)
			self.fetcher.update_data();
		
		self.con.root.Machine(self.fetcher.summary["name"], 7200, self.fetcher.update_data);
		

	
	def datalog(self):
		from time import sleep
		while self.datalogger:
			
			#self.data_sum = self.fetcher.update_data();
			#self.con.root.reg_workstation(self.data_sum)
			sleep(1);
		
		
		
		

if __name__ == '__main__':
	
	from multiprocessing import Process
	
	client = cliente("Motorhome", 8082);
	
	fetch_thread = Process(target=client.fetch_work, args=(1,))
	fetch_thread.start()
	
	

