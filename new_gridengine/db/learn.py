#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#       sem título.py
#       
#       Copyright 2011  <eduardo@Motorhome>
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



def main():
	
	import sqlalchemy as sa

	engine = sa.create_engine('sqlite:///:memory:',echo=True )

	metausers = sa.MetaData()
	metamachines = sa.MetaData()
	metawork = sa.MetaData()

	users_table = sa.Table('users', metausers, 
		sa.Column('id', sa.Integer, primary_key=True),
		sa.Column('name', sa.String(50)),
		sa.Column('fullname', sa.String(50)),
		sa.Column('passwd', sa.String(50))
	)
		
	machine_table = sa.Table('workstations', metamachines,
		sa.Column('id', sa.Integer, primary_key=True),
		sa.Column('key', sa.Integer),
		sa.Column('Cores', sa.Integer),
		sa.Column('Memory', sa.Integer),
		sa.Column('HD', sa.Integer),
		sa.Column('load',sa.Integer),
		sa.Column('Name', sa.String(50)),
		sa.Column('TotalWorks', sa.Integer)
	)

	work_table = sa.Table('workunits', metawork,
		sa.Column('id', sa.Integer, primary_key=True),
		sa.Column('prog', sa.String(50)),
		sa.Column('input', sa.Binary),
		sa.Column('output', sa.Binary),
		sa.Column('status', sa.Integer),
		sa.Column('worker', sa.Integer)
	)
	metausers.create_all(engine)	
	metamachines.create_all(engine)
	metawork.create_all(engine)

	
	return 0

if __name__ == '__main__':
	main()

