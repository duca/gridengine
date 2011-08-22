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
import logging, sys;
class logger:

	calee = None;
	
	def __init__(self,fname):
		
		logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s ', filename=fname, level=logging.CRITICAL);	
	
	def reg(self, message, level):		
		if level == 0:
			logging.warning(message)
		elif level == 1:
			logging.error(message)
		elif level == 2:
			logging.critical(message)
		else:
			logging.critical(message)
		sys.stderr.write(message+"\n")
		
	
	

