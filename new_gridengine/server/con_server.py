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
import erros, rpyc, rrdb

class mainService(rpyc.Service):
	
	class exposed_Machine(object):
		def __init__(self, st_name, st_samplespday, data_callback):
			
			from multiprocessing import Process, Pipe
			import rpyc
			
			self.machine = st_name;
			self.machsummary = {};
			self.samplespday = st_samplespday;
			self.active = True;
			self.callback = data_callback;
			self.ctrlPipe = Pipe();

			self.errorl = erros.logger("server_erros.log");
			self.errorl.calee = "Server: mainService(__init__)";			
			self.machsummary = self.callback();
			delay = 24*60*60/samplespday;
			thrd = Process(target=self.worker());
			thrd.start();
		def on_connect(self):
			
			self.errorl.reg("Someone Connected",1)			
			
			
		def exposed_reg_workstation(self, summary):
			
			self.errorl.reg("Registering: ",1)
			
			
		
		def worker(self):			
			import time
			
			while self.active:				
				self.machsummary = self.callback();								
				time.sleep(self.delay);				
				print self.machsummary;
				
				
				
	
	

if __name__ == '__main__':
	from rpyc.utils.server import ThreadedServer
	
	ThreadedServer(mainService, port=8082).start()
	
