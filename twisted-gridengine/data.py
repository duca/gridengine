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

class Fetcher:

	def __init__(self, delay):
		import erros
	
		self.logger = erros.logger('erro.log')
		self.logger.calee = 'fetch';
		self.summary = {};		
		self.delay = delay;
		self.active = True;
		
	def fetch(self):
		import os, erros, datetime
		from multiprocessing import cpu_count
		
		load = os.getloadavg()[0];
		hostname = os.uname()[1];
		kernel = os.uname()[2];
		cores = cpu_count();
		date = datetime.datetime.utcnow()
		
		load = load*100/cores;
		try:
			memory = os.popen("free -m").readlines()[1];
			total = int(memory.split()[1]);
			used = int(memory.split()[2]);
			cached = int(memory.split()[6]);
			free_ram = total - (used - cached);			
		except:
			total = 1000;
			free_ = 500;		
			self.logger.reg("Não foi possível obter os dados de memória ", 3);
			
		self.summary = { 'hostname': hostname, 'load': load, 
					'kernel': kernel, 'cores': cores, 'total_ram':total,
					'ava_ram':free_ram}
		return self.summary

	def fetch_loop(self, delay, pipe):
		import time;

		while self.active:
			try:
				pipe.send(self.fetch());
			except:
				text = "Cannot send data to mainloop at the " + str(i) + "th iteration";
				self.logger.reg(text, 1);		

			time.sleep(delay);	 	

	def work_start(self):
		from multiprocessing import Process, Pipe
		
		self.ppipe, chipipe = Pipe()
		self.p = Process(target=self.fetch_loop, args=(self.delay,chipipe));
		self.p.start();
	
	def restart_loop(self):
		
		self.active = True;
		self.p.start();
			
	def stop_loop(self):
		
		self.active = False;		
		self.p.terminate();
		
	def update_data(self):
		
		self.summary = self.ppipe.recv();		
		return self.summary;
	
	
class clientDB():
	""" Class doc """
	
	def __init__ (self):
		""" Class initialiser """
		self.client = 0;
		self.load = 0;
		self.data = []

		
	def update(self, client, load):
		
		self.data.append({client, load})
		
	def remove(self,client):
		
		for node in self.data:
			if node[client] != NULL:
				self.data.pop(node)

	
if __name__ == '__main__':
	import erros, sys, time
	from multiprocessing import Process, Pipe
	
	datalog = Fetcher(0);
	datalog.work_start();
	time.sleep(3);	
	
	datalog.update_data();
	print datalog.summary;		
	datalog.stop_loop();	

	sys.exit()

