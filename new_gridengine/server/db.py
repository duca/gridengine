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
import db
import sqlalchemy as sa

class workstationDB:
	
	
	def __init__(filename):
		
		self.engine = sa.create_engine('sqlite:///:memory:',echo=True);
		metamachines = sa.MetaData();
		machine_table = sa.Table ('workstations', metamachines,
		sa.Column('id', sa.Integer, primary_key=True),
		sa.Column('key', sa.Integer),
		sa.Column('Cores', sa.Integer),
		sa.Column('Memory', sa.Integer),
		sa.Column('HD', sa.Integer),
		sa.Column('load',sa.Integer),
		sa.Column('Name', sa.String(50)),
		sa.Column('TotalWorks', sa.Integer)		

if __name__ == '__main__':
	
	test = dataService('localhost', 1000)
	

